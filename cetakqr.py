from escpos.printer import File
#from espos import *
import json
import requests
import time


def cetakstruk():

    response = requests.get('https://apikaltimtara.adminparkir.web.id/hasil.php')
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
while True:
  time.sleep(1)
  try:
    cetakstruk()
  except:
    print('error')
  
