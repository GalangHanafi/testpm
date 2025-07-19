from escpos.printer import File
#from espos import *
import json
import requests
import time
import RPi.GPIO as GPIO
import signal

# GLOBAL VARIABLE
IS_PRESSED = 0
INPUT_PINS = [12, 16, 17, 20, 21, 27]

def get_unpaid_qris() -> dict | None:
    url = "26.46.181.23:8000/dutaparkir/getunpaidqris.php"

    try:
        response = requests.request("GET", url)
        return response.json()
    except Exception as e:
        print("❌ Gagal get unpaid qris: ", e)
        return None

def callback_manual_qris(qris_id: str) -> None:
    print("callback qris: ", qris_id)
    url = "26.46.181.23:8000/dutaparkir/QRIS/callback.php"
    payload = f'kode={qris_id}'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    try:
        requests.request("POST", url, headers=headers, data=payload)
        print("✔️ callback qris: ", qris_id, "selesai")
    except Exception as e:
        print("❌ Gagal callback qris: ", e)


def call_tombol(channel: int) -> None:
    global IS_PRESSED
    print("tombol ditekan")
    
    IS_PRESSED = 1
    if IS_PRESSED:
        return

    while IS_PRESSED:
        unpaid_qris = get_unpaid_qris()

        if not unpaid_qris:
            IS_PRESSED = 0

        for qris in unpaid_qris:
            callback_manual_qris(qris['id_tagihan'])

try:
    GPIO.setmode(GPIO.BCM)
    for pin in INPUT_PINS:
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(pin, GPIO.FALLING, callback=call_tombol, bouncetime=250)

    print("📡 Menunggu tombol ditekan...")
    signal.pause()
except Exception as e:
    print ("Error: ", e)
finally:
    GPIO.cleanup()

# kita pencet tombol apapun
# kita set button is pressed = 1
# kita set juga time 
# while button is pressed = 1
#   kita get_unpaid_qris 30 menit kebelakang
#   callback manual qris
#   if !unpaid_qris
#     set button is pressed = 0