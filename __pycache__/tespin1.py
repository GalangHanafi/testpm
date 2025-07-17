import RPi.GPIO as GPIO
import time
import pygame

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(27,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(22,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(18,GPIO.OUT,initial=GPIO.LOW)

pygame.mixer.init()


def call_dispenser(channel):
    if (GPIO.input(17)==0):
        print('GPIO 17 on Sensor/Loop')
    if (GPIO.input(17)==1):
        print('GPIO 17 off Sensor/Loop')
        
    
def call_tombol(channel):
    if (GPIO.input(27)==0):
        print('GPIO 27 on Tombol')
    if (GPIO.input(27)==1):
        print('GPIO 27 off Tombol')
    
def call_palang(channel):
    if (GPIO.input(22)==0):
        print('GPIO 22 on Palang')
    if (GPIO.input(22)==1):
        print('GPIO 22 off Palang')

    
    

try:    
    GPIO.add_event_detect(17, GPIO.BOTH, callback=call_dispenser, bouncetime=76)
    GPIO.add_event_detect(27, GPIO.BOTH, callback=call_tombol, bouncetime=76)
    GPIO.add_event_detect(22, GPIO.BOTH, callback=call_palang, bouncetime=76)
    while True:
        time.sleep(0.5)


except ValueError:
    print ("Bermasalah")


    

