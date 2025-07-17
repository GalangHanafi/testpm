from escpos.printer import File
from escpos.espos import *
import sys
import datetime
from datetime import datetime

import RPi.GPIO as GPIO
import urllib
import urllib.request
import os
#import treading
import time

import pygame
#amixer sset PCM,0 100%
import socket
socket.setdefaulttimeout(2)

import json
import requests

import pycurl
from io import BytesIO
from io import StringIO

import logging

import ipget
a = ipget.ipget ()
iplokal = a.ipaddr ("eth0")

tombol = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(16,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(20,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(21,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(27,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(18,GPIO.OUT,initial=GPIO.LOW)

pygame.mixer.init()
t = pygame.mixer.Sound("/home/pi/parkir/tombol.wav")
m= pygame.mixer.Sound("/home/pi/parkir/masuk.wav")

t.play()
print('suara')

def main():
    print ("Bismillah")

def tokennya():
    url = "https://apikaltimtara.adminparkir.web.id/Auth.php"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)

    url = "https://apikaltimtara.adminparkir.web.id/Auth-b2b.php"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)

    
def call_tombol(channel):
#def call_a():
    print ('coba')
#def coba():
    global tombol
    global datang
    global masuk

 
    #if (GPIO.input(27)==1 ):
#         serverduta()
    print ('tombol')
    print (tombol)

    if (GPIO.input(12)==0 or GPIO.input(16)==0 or GPIO.input(17)==0 or GPIO.input(20)==0 or GPIO.input(21)==0 or GPIO.input(27)==0):

        if GPIO.input(16)== 0:
          jenisk = 'CRANE /ALATBERAT BAN KARET'
        if GPIO.input(17) == 0:
          jenisk ='ALAT BERAT BAN RANTAI'
        if GPIO.input(20)== 0:
          jenisk = 'TRUK TRAILER'
        if GPIO.input(21) == 0:
          jenisk ='RODA 6/LEBIH'
        if GPIO.input(27)== 0:
          jenisk = 'FORKLIFT'
        if GPIO.input(12) == 0:
          jenisk ='RODA 4'
     #   ijin()
        print(jenisk)
        url = 'https://apikaltimtara.adminparkir.web.id/cektarif.php'
        payload = {'jenisk' : jenisk}
        headers = {'Content-Type': 'application/json'}
        param = ( ('priority','normal'), )
        response = requests.post(url, data=(payload))
        re = response.json()
        print (re)
        rs_status = re['status']
        rs_kode = re['kode']
        rs_tarif = re['tarif']
        rs_waktu = re['waktu']

        if rs_status == '200':
#             url = "https://apikaltimtara.adminparkir.web.id/Auth.php"
# 
#             payload = {}
#             headers = {}
# 
#             response = requests.request("GET", url, headers=headers, data=payload)
# 
#             print(response.text)
# 
#             url = "https://apikaltimtara.adminparkir.web.id/Auth-b2b.php"
# 
#             payload = {}
#             headers = {}
# 
#             response = requests.request("GET", url, headers=headers, data=payload)
# 
#             print(response.text)
# 


            harga = int(rs_tarif)
            url = 'https://apikaltimtara.adminparkir.web.id/Qris-req.php'
            payload = {'kode' : rs_kode, 'amount' : harga, 'jenisk' : jenisk}
            print(url)
            print(payload)
            headers = {'Content-Type': 'application/json'}
            param = ( ('priority','normal'), )
            response = requests.post(url, data=(payload), timeout=9)
            re = response.json()
            print (re)
            
            if re['success'] == False:
                tokennya()
                response = requests.post(url, data=(payload), timeout=9)
                re = response.json()
                print (re)
                
 
        # 
            aa = re['data']['barcode']
        #     print(aa,'' ,5)
                
        #     except:
        #         print('error struk')
            
        #     if re['status']=='200':
            
            Epson = File("/dev/usb/lp0")
            Epson.text("\x1b\x45\x00") # font normal
            Epson.text("\x1b\x21\x00") # text normal
            Epson.text("\x1b\x4d\x01") #tipe font b
            Epson.text("\x1b\x21\x10") # double heiht text
           # Epson.text("\x1b\x21\x20") # double widht text
            Epson.text("\x1b\x61\x01")
            Epson.text("UPT PELABUHAN PENAJAM BULUMINUNG\n")
            Epson.text("Jalan Kapo, Kel Gunung Seteleng, Penajam\n\n")
            Epson.text("Waktu : ")
            Epson.text(rs_waktu)
            Epson.text("\n")
            

            Epson.qr(aa,size=8)
            Epson.text("Kode Trx : ")
            Epson.text(rs_kode)
            Epson.text("\n Jenis Kendaraan : ")
            Epson.text(jenisk)
            Epson.text("\n Tarif : Rp.")
            Epson.text(harga)
            Epson.cut()
            Epson.close()
            

             #   url = 'http://26.63.88.98/dutaparkir/Kaltimtara/Qris-req.php'

 

try:    
    GPIO.add_event_detect(12, GPIO.BOTH, callback=call_tombol, bouncetime=76)
    GPIO.add_event_detect(16, GPIO.BOTH, callback=call_tombol, bouncetime=76)
    GPIO.add_event_detect(17, GPIO.BOTH, callback=call_tombol, bouncetime=76)
    GPIO.add_event_detect(20, GPIO.BOTH, callback=call_tombol, bouncetime=76)
    GPIO.add_event_detect(21, GPIO.BOTH, callback=call_tombol, bouncetime=76)
    GPIO.add_event_detect(27, GPIO.BOTH, callback=call_tombol, bouncetime=76)
    while True:

        time.sleep(1)
except ValueError:
    print ("Bermasalah")