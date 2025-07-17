import RPi.GPIO as GPIO
import time
import pygame

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(27,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(22,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(18,GPIO.OUT,initial=GPIO.LOW)

pygame.mixer.init()
t = pygame.mixer.Sound("/home/pi/parkir/tombol.wav")
m= pygame.mixer.Sound("/home/pi/parkir/masuk.wav")

t.play()


def call_dispenser(channel):
    if (GPIO.input(17)==0):
        m.play()
        GPIO.output(18,1)
        time.sleep(0.5)
        GPIO.output(18,0)
        
    
def call_tombol(channel):
    if (GPIO.input(27)==0):
        t.play()
        GPIO.output(18,1)
        time.sleep(0.5)
        GPIO.output(18,0)
    
def call_palang(channel):
    if (GPIO.input(22)==0):
        GPIO.output(18,1)
        time.sleep(0.5)
        GPIO.output(18,0)
    
    

try:    
    GPIO.add_event_detect(17, GPIO.BOTH, callback=call_dispenser, bouncetime=76)
    GPIO.add_event_detect(27, GPIO.BOTH, callback=call_tombol, bouncetime=76)
    GPIO.add_event_detect(22, GPIO.BOTH, callback=call_palang, bouncetime=76)
    while True:
        time.sleep(0.7)
        print('ok')

except ValueError:
    print ("Bermasalah")


    

