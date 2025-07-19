# ---------------- DEKLARASI ----------------
import os
import time
import json
import socket
import requests
import pygame
import RPi.GPIO as GPIO
from escpos.printer import File
import ipget

# Konstanta dan variabel global
K_IPCAMERA = "192.168.1.111"
K_IPSERVER = "192.168.1.88"
URL_BASE = f"http://{K_IPSERVER}/dutaparkir"

QRIS_ID = None
JENIS_KENDARAAN = None
WAKTU_MULAI = time.time()

INPUT_PINS = [12, 16, 17, 20, 21, 27]
JENIS_MAP = {
    12: 'RODA 4',
    16: 'CRANE /ALATBERAT BAN KARET',
    17: 'ALAT BERAT BAN RANTAI',
    20: 'TRUK TRAILER',
    21: 'RODA 6/LEBIH',
    27: 'FORKLIFT'
}

# ---------------- SETUP ----------------
def setup():
    global SOUND_TOMBOL, SOUND_MASUK, IPLOKAL

    # Set timeout koneksi
    socket.setdefaulttimeout(2)

    # Inisialisasi IP lokal
    a = ipget.ipget()
    IPLOKAL = a.ipaddr("eth0")

    # Setup GPIO
    GPIO.setmode(GPIO.BCM)
    for pin in INPUT_PINS:
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)

    # Setup suara
    pygame.mixer.init()
    SOUND_TOMBOL = pygame.mixer.Sound("/home/pi/parkir/tombol.wav")
    SOUND_MASUK = pygame.mixer.Sound("/home/pi/parkir/masuk.wav")
    SOUND_TOMBOL.play()
    print("🔊 Suara tombol diputar")

    # Tambahkan event detect
    for pin in INPUT_PINS:
        GPIO.add_event_detect(pin, GPIO.FALLING, callback=call_tombol, bouncetime=250)

# ---------------- FUNGSI ----------------
def cetak_qr(kode, barcode, waktu, harga, jenisk):
    try:
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
        print(f"🧾 Cetak QRIS: {kode}")
    except Exception as e:
        print("🖨️ Gagal cetak struk:", e)

def insert_masuk(kode, waktu, jenis, bcd):
    try:
        payload = f'kode={kode}&waktu={waktu}&jenis={jenis}&bcd={bcd}'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        requests.post(f"{URL_BASE}/insertMasuk.php", headers=headers, data=payload)
    except Exception as e:
        print("❌ Gagal insert masuk:", e)

def simpan_gambar():
    try:
        if os.system(f"ping -c 1 {K_IPCAMERA}") == 0:
            requests.post(f"{URL_BASE}/fotom.php", data={'ip': K_IPCAMERA, 'nama': QRIS_ID})
    except Exception as e:
        print("📷 Gagal ambil gambar:", e)

def call_tombol(channel):
    global JENIS_KENDARAAN, QRIS_ID, WAKTU_MULAI

    if (time.time() - WAKTU_MULAI) < 2:
        return
    WAKTU_MULAI = time.time()

    JENIS_KENDARAAN = JENIS_MAP.get(channel)
    if not JENIS_KENDARAAN:
        print("⚠️ Tombol tidak dikenali:", channel)
        return

    try:
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        payload = f'jenisk={JENIS_KENDARAAN}'
        response = requests.post(f"{URL_BASE}/cektarif.php", headers=headers, data=payload)
        tarif_data = response.json()

        if tarif_data.get('status') != 200:
            print("❌ Tarif tidak ditemukan")
            return

        kode = tarif_data['kode']
        waktu = tarif_data['waktu']
        harga = int(tarif_data['tarif'])

        qris_payload = {'kode': kode, 'amount': harga}
        response = requests.post(f"{URL_BASE}/QRIS/Qris-req.php", headers=headers, data=qris_payload)
        qris_data = response.json()

        if 'data' not in qris_data or 'barcode' not in qris_data['data']:
            print("❌ Format QRIS error")
            return

        barcode = qris_data['data']['barcode']
        QRIS_ID = qris_data['data']['kode']

        print(f"✅ QRIS ID: {QRIS_ID}")
        cetak_qr(kode, barcode, waktu, harga, JENIS_KENDARAAN)
        SOUND_MASUK.play()
        insert_masuk(kode, waktu, JENIS_KENDARAAN, QRIS_ID)
        simpan_gambar()

    except Exception as e:
        print("🛑 Error tombol:", e)

# ---------------- LOOP ----------------
def loop():
    print("🚦 Sistem siap. Menunggu kendaraan masuk...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n⛔ Dihentikan pengguna (Ctrl+C)")
    except Exception as e:
        print("🛑 Error utama:", e)
    finally:
        GPIO.cleanup()
        print("🧹 GPIO dibersihkan")

# ---------------- MAIN ----------------
if __name__ == "__main__":
    setup()
    loop()
