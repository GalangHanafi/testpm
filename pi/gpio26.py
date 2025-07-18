import RPi.GPIO as GPIO
import time
import pygame

GPIO.setmode(GPIO.BCM)
GPIO.setup(0,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
##GPIO.setup(2,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
##GPIO.setup(3,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(4,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(5,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(6,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(7,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(8,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(9,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(10,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(11,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(14,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(15,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(16,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(19,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(20,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(21,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(22,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(23,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(25,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(26,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(27,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)


##GPIO.setup(18,GPIO.OUT,initial=GPIO.LOW)

pygame.mixer.init()


def call_0(channel):
    if (GPIO.input(0)==0):
        print('GPIO-PIN 0 ON status = 0')
    if (GPIO.input(0)==1):
        print('GPIO-PIN 0 OFF status = 1')

def call_1(channel):
    if (GPIO.input(1)==0):
        print('GPIO-PIN 1 ON status = 0')
    if (GPIO.input(1)==1):
        print('GPIO-PIN 1 OFF status = 1')

##def call_2(channel):
##    if (GPIO.input(2)==0):
##        print('GPIO-PIN 2 ON status = 0')
##    if (GPIO.input(2)==1):
##        print('GPIO-PIN 2 OFF status = 1')
##
##def call_3(channel):
##    if (GPIO.input(3)==0):
##        print('GPIO-PIN 3 ON status = 0')
##    if (GPIO.input(3)==1):
##        print('GPIO-PIN 3 OFF status = 1')

def call_4(channel):
    if (GPIO.input(4)==0):
        print('GPIO-PIN 4 ON status = 0')
    if (GPIO.input(4)==1):
        print('GPIO-PIN 4 OFF status = 1')

def call_5(channel):
    if (GPIO.input(5)==0):
        print('GPIO-PIN 5 ON status = 0')
    if (GPIO.input(5)==1):
        print('GPIO-PIN 5 OFF status = 1')

def call_6(channel):
    if (GPIO.input(6)==0):
        print('GPIO-PIN 6 ON status = 0')
    if (GPIO.input(6)==1):
        print('GPIO-PIN 6 OFF status = 1')

def call_7(channel):
    if (GPIO.input(7)==0):
        print('GPIO-PIN 7 ON status = 0')
    if (GPIO.input(7)==1):
        print('GPIO-PIN 7 OFF status = 1')

def call_8(channel):
    if (GPIO.input(8)==0):
        print('GPIO-PIN 8 ON status = 0')
    if (GPIO.input(8)==1):
        print('GPIO-PIN 8 OFF status = 1')

def call_9(channel):
    if (GPIO.input(9)==0):
        print('GPIO-PIN 9 ON status = 0')
    if (GPIO.input(9)==1):
        print('GPIO-PIN 9 OFF status = 1')

def call_10(channel):
    if (GPIO.input(10)==0):
        print('GPIO-PIN 10 ON status = 0')
    if (GPIO.input(10)==1):
        print('GPIO-PIN 10 OFF status = 1')

def call_11(channel):
    if (GPIO.input(11)==0):
        print('GPIO-PIN 11 ON status = 0')
    if (GPIO.input(11)==1):
        print('GPIO-PIN 11 OFF status = 1')

def call_12(channel):
    if (GPIO.input(12)==0):
        print('GPIO-PIN 12 ON status = 0')
    if (GPIO.input(12)==1):
        print('GPIO-PIN 12 OFF status = 1')

def call_13(channel):
    if (GPIO.input(13)==0):
        print('GPIO-PIN 13 ON status = 0')
    if (GPIO.input(13)==1):
        print('GPIO-PIN 13 OFF status = 1')

def call_14(channel):
    if (GPIO.input(14)==0):
        print('GPIO-PIN 14 ON status = 0')
    if (GPIO.input(14)==1):
        print('GPIO-PIN 14 OFF status = 1')

def call_15(channel):
    if (GPIO.input(15)==0):
        print('GPIO-PIN 15 ON status = 0')
    if (GPIO.input(15)==1):
        print('GPIO-PIN 15 OFF status = 1')

def call_16(channel):
    if (GPIO.input(16)==0):
        print('GPIO-PIN 16 ON status = 0')
    if (GPIO.input(16)==1):
        print('GPIO-PIN 16 OFF status = 1')

def call_17(channel):
    if (GPIO.input(17)==0):
        print('GPIO-PIN 17 ON status = 0')
    if (GPIO.input(17)==1):
        print('GPIO-PIN 17 OFF status = 1')

def call_18(channel):
    if (GPIO.input(18)==0):
        print('GPIO-PIN 18 ON status = 0')
    if (GPIO.input(18)==1):
        print('GPIO-PIN 18 OFF status = 1')

def call_19(channel):
    if (GPIO.input(19)==0):
        print('GPIO-PIN 19 ON status = 0')
    if (GPIO.input(19)==1):
        print('GPIO-PIN 19 OFF status = 1')

def call_20(channel):
    if (GPIO.input(20)==0):
        print('GPIO-PIN 20 ON status = 0')
    if (GPIO.input(20)==1):
        print('GPIO-PIN 20 OFF status = 1')

def call_21(channel):
    if (GPIO.input(21)==0):
        print('GPIO-PIN 21 ON status = 0')
    if (GPIO.input(21)==1):
        print('GPIO-PIN 21 OFF status = 1')

def call_22(channel):
    if (GPIO.input(22)==0):
        print('GPIO-PIN 22 ON status = 0')
    if (GPIO.input(22)==1):
        print('GPIO-PIN 22 OFF status = 1')

def call_23(channel):
    if (GPIO.input(23)==0):
        print('GPIO-PIN 23 ON status = 0')
    if (GPIO.input(23)==1):
        print('GPIO-PIN 23 OFF status = 1')

def call_24(channel):
    if (GPIO.input(24)==0):
        print('GPIO-PIN 24 ON status = 0')
    if (GPIO.input(24)==1):
        print('GPIO-PIN 24 OFF status = 1')

def call_25(channel):
    if (GPIO.input(25)==0):
        print('GPIO-PIN 25 ON status = 0')
    if (GPIO.input(25)==1):
        print('GPIO-PIN 25 OFF status = 1')

def call_26(channel):
    if (GPIO.input(26)==0):
        print('GPIO-PIN 26 ON status = 0')
    if (GPIO.input(26)==1):
        print('GPIO-PIN 26 OFF status = 1')
    
def call_27(channel):
    if (GPIO.input(27)==0):
        print('GPIO-PIN 27 ON status = 0')
    if (GPIO.input(27)==1):
        print('GPIO-PIN 27 OFF status = 1')

try:    
    GPIO.add_event_detect(0, GPIO.BOTH, callback=call_0, bouncetime=76)
    GPIO.add_event_detect(1, GPIO.BOTH, callback=call_1, bouncetime=76)
##    GPIO.add_event_detect(2, GPIO.BOTH, callback=call_2, bouncetime=76)
##    GPIO.add_event_detect(3, GPIO.BOTH, callback=call_3, bouncetime=76)
    GPIO.add_event_detect(4, GPIO.BOTH, callback=call_4, bouncetime=76)
    GPIO.add_event_detect(5, GPIO.BOTH, callback=call_5, bouncetime=76)
    GPIO.add_event_detect(6, GPIO.BOTH, callback=call_6, bouncetime=76)
    GPIO.add_event_detect(7, GPIO.BOTH, callback=call_7, bouncetime=76)
    GPIO.add_event_detect(8, GPIO.BOTH, callback=call_8, bouncetime=76)
    GPIO.add_event_detect(9, GPIO.BOTH, callback=call_9, bouncetime=76)
    GPIO.add_event_detect(10, GPIO.BOTH, callback=call_10, bouncetime=76)
    GPIO.add_event_detect(11, GPIO.BOTH, callback=call_11, bouncetime=76)
    GPIO.add_event_detect(12, GPIO.BOTH, callback=call_12, bouncetime=76)
    GPIO.add_event_detect(13, GPIO.BOTH, callback=call_13, bouncetime=76)
    GPIO.add_event_detect(14, GPIO.BOTH, callback=call_14, bouncetime=76)
    GPIO.add_event_detect(15, GPIO.BOTH, callback=call_15, bouncetime=76)
    GPIO.add_event_detect(16, GPIO.BOTH, callback=call_16, bouncetime=76)
    GPIO.add_event_detect(17, GPIO.BOTH, callback=call_17, bouncetime=76)
    GPIO.add_event_detect(18, GPIO.BOTH, callback=call_18, bouncetime=76)
    GPIO.add_event_detect(19, GPIO.BOTH, callback=call_19, bouncetime=76)
    GPIO.add_event_detect(20, GPIO.BOTH, callback=call_20, bouncetime=76)
    GPIO.add_event_detect(21, GPIO.BOTH, callback=call_21, bouncetime=76)
    GPIO.add_event_detect(22, GPIO.BOTH, callback=call_22, bouncetime=76)
    GPIO.add_event_detect(23, GPIO.BOTH, callback=call_23, bouncetime=76)
    GPIO.add_event_detect(24, GPIO.BOTH, callback=call_24, bouncetime=76)
    GPIO.add_event_detect(25, GPIO.BOTH, callback=call_25, bouncetime=76)
    GPIO.add_event_detect(26, GPIO.BOTH, callback=call_26, bouncetime=76)
    GPIO.add_event_detect(27, GPIO.BOTH, callback=call_27, bouncetime=76)
    while True:
        time.sleep(0.5)


except ValueError:
    print ("Bermasalah")


    

