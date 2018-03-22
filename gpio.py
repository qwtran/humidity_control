import time
import RPi.GPIO as GPIO 

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(11, GPIO.OUT)

while True:
	GPIO.output(11, True)
	time.sleep(5)
	GPIO.output(11, False)
	time.sleep(5)

#GPIO.cleanup()
