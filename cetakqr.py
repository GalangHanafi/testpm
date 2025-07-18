from escpos.printer import File
#from espos import *
import json
import requests
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)

def cetakstruk():
    print("cetakstruk")
    response = requests.get('http://192.168.1.88:8000/dutaparkir/cekbayar__.php')
    print(response)
    re = (response.json()) 
    print(re)

    if re['status']=='200':
      
        Epson = File("/dev/usb/lp0")
        Epson.text("\x1b\x45\x00") # font normal
        Epson.text("\x1b\x21\x00") # text normal
        Epson.text("\x1b\x4d\x01") #tipe font b
        Epson.text("\x1b\x21\x10") # double heiht text
       # Epson.text("\x1b\x21\x20") # double widht text
        Epson.text("\x1b\x61\x01")
        Epson.text("UPT PELABUHAN PENAJAM BULUMINUNG\n")
        Epson.text("Jalan Kapo, Kel Gunung Seteleng, Penajam\n\n")
        jenisk = re['jenisk']
        Epson.text(jenisk)
        
        Epson.text('\n')
        Epson.text('Rp.')
        tarif= re['amount']
        Epson.text(tarif)
        Epson.text(',-')
        Epson.text('\n\n')
        Epson.text("\x1b\x45\x00") # font normal
        Epson.text("\x1b\x21\x00") # text normal
        Epson.text("\x1b\x4d\x01") #tipe font b
        Epson.text('Kode Transaksi: ')
        Epson.text(re['kode'])
        Epson.text('\n Waktu: ')
        Epson.text(re['waktu'])
        
        Epson.cut()
        Epson.close()
        
        return True
    
def buka_palang():
    GPIO.output(18, GPIO.HIGH)
    time.sleep(1000)
    GPIO.output(18, GPIO.LOW)

while True:
    time.sleep(1)
    try:
        cetakstruk = cetakstruk()
        if cetakstruk:
            buka_palang()
        
    except KeyboardInterrupt:
        print("Keluar program")
        GPIO.cleanup()
    except:
        print('error')
  