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

Epson = File("/dev/usb/lp0")
Epson.text("\x1b\x4d\x00") #tipe font b
Epson.text("\x1b\x45\x01") #fontblod
Epson.text("\x1b\x21\x10") # double heiht text
Epson.text("\x1b\x61\x01")
Epson.text("TES CETAK TIKET\n")
Epson.text("\n")
Epson.text("\x1b\x45\x00") # font normal
Epson.text("\x1b\x21\x00") # text normal
Epson.cut()


