import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(23,GPIO.OUT,initial=GPIO.LOW)

GPIO.output(18,1)
print('Relay NO Tutup')
time.sleep(1)
GPIO.output(18,0)
print('Relay NO Buka')
time.sleep(1)

