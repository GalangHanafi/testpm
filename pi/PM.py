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
K_IPCAMERA = "192.168.1.111"  # ganti sesuai IP camera
K_IPSERVER = "192.168.1.88"
WAKTU_MULAI = time.time()

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

def insert_masuk(kode, waktu, jenis, bcd):
    url = "http://192.168.1.88:8000/dutaparkir/insertMasuk.php"

    payload = f'kode={kode}&waktu={waktu}&jenis={jenis}&bcd={bcd}'
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    # print("================================")
    # print("insertMasuk: ", response)
    # print("================================")

def call_tombol(channel):
    global TOMBOL_AKTIF, JENIS_KENDARAAN, QRIS_ID, WAKTU_MULAI

    if (time.time() - WAKTU_MULAI) > 2:
        WAKTU_MULAI = time.time()
        
        TOMBOL_AKTIF = 1

        jenis_map = {
            12: 'RODA 4',
            16: 'CRANE /ALATBERAT BAN KARET',
            17: 'ALAT BERAT BAN RANTAI',
            20: 'TRUK TRAILER',
            21: 'RODA 6/LEBIH',
            27: 'FORKLIFT'
        }

        if channel in jenis_map:
            TOMBOL_AKTIF = 1
            JENIS_KENDARAAN = jenis_map[channel]
        else:
            # print("Channel tidak dikenal")
            return  # keluar dari fungsi

        # print(f"Jenis kendaraan: {JENIS_KENDARAAN}")

        payload = 'jenisk=RODA%204'
        headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
        }

        #  CEK TARIF
        response = requests.request("POST", "http://192.168.1.88:8000/dutaparkir/cektarif.php", headers=headers, data=payload)
        # print("=================")
        # print("cektarif: ", response)
        # print("=================")
        tarif_data = response.json()

        # print(f"Tarif data: {tarif_data}")

        # try:
        if tarif_data['status'] == 200:
            kode = tarif_data['kode']
            waktu = tarif_data['waktu']
            harga = int(tarif_data['tarif'])
            harga = int(harga)
            payload = {
                'kode': kode,
                'amount': harga
            }
            headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
            }
            
            # print("===============")
            # print("payload", payload)
            # print("===============")

            response = requests.request("POST", "http://192.168.1.88:8000/dutaparkir/QRIS/Qris-req.php", headers=headers, data=payload)
            # print("========================")
            # print("qris-req: ", response)
            # print("========================")
            qris_data = response.json()
            
            # print("======================")
            # print("qris-data: ", qris_data)
            barcode = qris_data['data']['barcode']
            QRIS_ID = qris_data['data']['kode']
            
            # print("===============================")
            # print("barcode: ", barcode)
            # print("QRIS_ID: ", QRIS_ID)
            # print("===============================")

            print(f"QRIS ID: {QRIS_ID}")
            cetak_qr(kode, barcode, waktu, harga, JENIS_KENDARAAN)
            print("SUDAH CETAK QRIS")
            SOUND_MASUK.play()

            insert_masuk(kode, waktu, JENIS_KENDARAAN, QRIS_ID)
                # TOMBOL_AKTIF = 1
        # except Exception as e:
            # print("Error saat mengambil QRIS:", e)
        # print("Menunggu tombol ditekan...")

        TOMBOL_AKTIF = 0

def cek_pembayaran():
    global QRIS_ID, JENIS_KENDARAAN, TOMBOL_AKTIF

    try:
        payload = f'jenis={JENIS_KENDARAAN}&qris_id={QRIS_ID}'
        headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.request("POST", "http://192.168.1.88:8000/dutaparkir/cekbayar.php", headers=headers, data=payload)
        # print("================================")
        # print("cekbayar: ", response)
        # print("================================")
        result = response.json()

        if result.get("success") == True:
            return True
        return False
    except Exception as e:
        # print("Gagal cek pembayaran:", e)
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

# time.sleep(5)
# call_tombol(12)

try:
    for pin in INPUT_PINS:
        GPIO.add_event_detect(pin, GPIO.FALLING, callback=call_tombol, bouncetime=250)

    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("Keluar program")
except Exception as e:
    print("Error utama:", e)
finally:
    GPIO.cleanup()
