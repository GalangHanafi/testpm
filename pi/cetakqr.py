from escpos.printer import File
#from espos import *
import json
import requests
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)

def cetakstruk():
    response = requests.get('http://192.168.1.88:8000/dutaparkir/cekbayar.php')
    print(response)
    re = (response.json()) 
    print(re)

    if re['success']:
        print("cetakstruk")
        Epson = File("/dev/usb/lp0")
        Epson.text("\x1b\x45\x00") # font normal
        Epson.text("\x1b\x21\x00") # text normal
        Epson.text("\x1b\x4d\x01") #tipe font b
        Epson.text("\x1b\x21\x10") # double heiht text
       # Epson.text("\x1b\x21\x20") # double widht text
        Epson.text("\x1b\x61\x01")
        Epson.text("UPT PELABUHAN PENAJAM BULUMINUNG\n")
        Epson.text("Jalan Kapo, Kel Gunung Seteleng, Penajam\n\n")
        jenisk = re['data']['jenisk']
        Epson.text(jenisk)
        
        Epson.text('\n')
        Epson.text('Rp.')
        tarif= re['data']['amount']
        Epson.text(tarif)
        Epson.text(',-')
        Epson.text('\n\n')
        Epson.text("\x1b\x45\x00") # font normal
        Epson.text("\x1b\x21\x00") # text normal
        Epson.text("\x1b\x4d\x01") #tipe font b
        Epson.text('Kode Transaksi: ')
        Epson.text(re['data']['kode'])
        Epson.text('\n Waktu: ')
        Epson.text(re['data']['waktu'])
        
        Epson.cut()
        Epson.close()
        
        print("sudah cetak")
        return True
    
def buka_palang():
    print("buka palang")
    GPIO.output(18, GPIO.HIGH)
    time.sleep(5)
    print("tutup palang")
    GPIO.output(18, GPIO.LOW)

while True:
    try:
        if cetakstruk():
            buka_palang()
        
    except KeyboardInterrupt:
        print("Keluar program")
        GPIO.cleanup()
    except Exception as e:
        print("===================================================")
        print('error')
        print("===================================================")
        print(e)
        GPIO.cleanup()

    time.sleep(5)
  