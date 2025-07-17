from escpos.printer import Usb
#from espos import *
import json
import requests
import time


url = 'https://apikaltimtara.adminparkir.web.id/Qris-req.php'
payload = {'kode' : '3333', 'amount' : 1300}

headers = {'Content-Type': 'application/json'}
param = ( ('priority','normal'), )
response = requests.post(url, data=(payload), timeout=9)
re = response.json()
print (re)

def cetakstruk():


     #   url = 'http://26.63.88.98/dutaparkir/Kaltimtara/Qris-req.php'
    url = 'https://apikaltimtara.adminparkir.web.id/callback.php'
    payload = {'kode' : '0505205222399'}
    print(url)
    print(payload)
    headers = {'Content-Type': 'application/json'}
    param = ( ('priority','normal'), )
    response = requests.post(url, data=(payload), timeout=9)
    re = response.json()
    print (re)

##    
##    
##    Epson = Usb(0x04B8,0x0E0B, 0)
##    Epson.text("\x1b\x45\x00") # font normal
##    Epson.text("\x1b\x21\x00") # text normal
##    Epson.text("\x1b\x4d\x01") #tipe font b
##    Epson.text("\x1b\x21\x10") # double heiht text
##   # Epson.text("\x1b\x21\x20") # double widht text
##    Epson.text("\x1b\x61\x01")
##    
##
##    Epson.qr(aa,size=8)
##    Epson.cut()
while True:
   # cetakstruk()
    time.sleep(2)