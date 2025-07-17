import os
import sys
import time
import json
import socket
import requests
import pycurl
import urllib.request
import pygame
import RPi.GPIO as GPIO
from io import BytesIO
from escpos.printer import File
import ipget

# ---------------- CONFIG ----------------
socket.setdefaulttimeout(2)
a = ipget.ipget()
iplokal = a.ipaddr("eth0")

QRIS_ID = ""
JENIS_KENDARAAN = ""
TOMBOL_AKTIF = 0
K_IPCAMERA = "192.168.1.100"  # ganti sesuai IP camera
K_IPSERVER = "apikaltimtara.adminparkir.web.id"

# ---------------- SETUP ----------------
GPIO.setmode(GPIO.BCM)
INPUT_PINS = [12, 16, 17, 20, 21, 27]
for pin in INPUT_PINS:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)

pygame.mixer.init()
SOUND_TOMBOL = pygame.mixer.Sound("/home/pi/parkir/tombol.wav")
SOUND_MASUK = pygame.mixer.Sound("/home/pi/parkir/masuk.wav")

SOUND_TOMBOL.play()
print("Suara tombol diputar")

# ---------------- FUNGSI ----------------
def ambil_token():
    for endpoint in ["Auth.php", "Auth-b2b.php"]:
        try:
            response = requests.get(f"https://{K_IPSERVER}/{endpoint}")
            print(f"Token response ({endpoint}):", response.text)
        except Exception as e:
            print(f"Token Error ({endpoint}):", e)

def cetak_qr(kode, barcode, waktu, harga, jenisk):
    Epson = File("/dev/usb/lp0")
    Epson.text("\x1b\x45\x00\x1b\x21\x00\x1b\x4d\x01\x1b\x21\x10\x1b\x61\x01")
    Epson.text("UPT PELABUHAN PENAJAM BULUMINUNG\n")
    Epson.text("Jalan Kapo, Kel Gunung Seteleng, Penajam\n\n")
    Epson.text(f"Waktu : {waktu}\n")
    Epson.qr(barcode, size=8)
    Epson.text(f"Kode Trx : {kode}\n")
    Epson.text(f"Jenis Kendaraan : {jenisk}\n")
    Epson.text(f"Tarif : Rp.{harga}\n")
    Epson.cut()
    Epson.close()

def call_tombol(channel):
    global TOMBOL_AKTIF, JENIS_KENDARAAN, QRIS_ID

    if TOMBOL_AKTIF:
        return

    jenis_map = {
        12: 'RODA 4',
        16: 'CRANE /ALATBERAT BAN KARET',
        17: 'ALAT BERAT BAN RANTAI',
        20: 'TRUK TRAILER',
        21: 'RODA 6/LEBIH',
        27: 'FORKLIFT'
    }

    for pin, jenis in jenis_map.items():
        if GPIO.input(pin) == 0:
            JENIS_KENDARAAN = jenis
            break
    else:
        return

    print(f"Jenis kendaraan: {JENIS_KENDARAAN}")

    try:
        tarif_response = requests.post(
            f"https://{K_IPSERVER}/cektarif.php",
            data={'jenisk': JENIS_KENDARAAN},
            timeout=5
        )
        tarif_data = tarif_response.json()

        if tarif_data['status'] == '200':
            kode = tarif_data['kode']
            waktu = tarif_data['waktu']
            harga = int(tarif_data['tarif'])

            qris_response = requests.post(
                f"https://{K_IPSERVER}/Qris-req.php",
                data={'kode': kode, 'amount': harga, 'jenisk': JENIS_KENDARAAN},
                timeout=9
            )
            qris_data = qris_response.json()

            if not qris_data.get('success'):
                ambil_token()
                qris_response = requests.post(
                    f"https://{K_IPSERVER}/Qris-req.php",
                    data={'kode': kode, 'amount': harga, 'jenisk': JENIS_KENDARAAN},
                    timeout=9
                )
                qris_data = qris_response.json()

            barcode = qris_data['data']['barcode']
            QRIS_ID = qris_data['data']['qris_id']

            cetak_qr(kode, barcode, waktu, harga, JENIS_KENDARAAN)
            SOUND_MASUK.play()
            TOMBOL_AKTIF = 1
    except Exception as e:
        print("Error saat mengambil tarif atau QRIS:", e)

def cek_pembayaran():
    global QRIS_ID, JENIS_KENDARAAN, TOMBOL_AKTIF

    try:
        response = requests.post(
            "http://localhost:8000/dutaparkir/cekbayar.php",
            data={'jenis': JENIS_KENDARAAN, 'qris_id': QRIS_ID},
            timeout=3
        )
        result = response.json()

        if result.get("success") == True:
            return True
        return False
    except Exception as e:
        print("Gagal cek pembayaran:", e)
        return False

def simpan_gambar():
    try:
        if os.system(f"ping -c 1 {K_IPCAMERA}") == 0:
            requests.post(
                f"http://{K_IPSERVER}/dutaparkir/fotom.php",
                data={'ip': K_IPCAMERA, 'nama': QRIS_ID}
            )
    except Exception as e:
        print("Kamera bermasalah:", e)

# ---------------- MAIN LOOP ----------------
try:
    for pin in INPUT_PINS:
        GPIO.add_event_detect(pin, GPIO.FALLING, callback=call_tombol, bouncetime=150)

    while True:
        sudah_bayar = cek_pembayaran()
        if sudah_bayar:
            print("Bayar sukses, buka pintu!")
            GPIO.output(18, GPIO.HIGH)
            time.sleep(1000)
            GPIO.output(18, GPIO.LOW)
            TOMBOL_AKTIF = 0
        # simpan_gambar()
        time.sleep(1000)

except KeyboardInterrupt:
    print("Keluar program")
    GPIO.cleanup()
except Exception as e:
    print("Error utama:", e)
    GPIO.cleanup()
