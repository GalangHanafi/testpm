
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(27,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(22,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

print('tes')
print("Sensor Status = ",GPIO.input(17))
print("Tombol Status = ",GPIO.input(27))
print("Palang Status = ",GPIO.input(22))
