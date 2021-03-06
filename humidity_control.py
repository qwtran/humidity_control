import sys
import time
import Adafruit_DHT
import RPi.GPIO as GPIO

RELAY_PIN = 11
TEMP_PIN  = 4

sensor = Adafruit_DHT.DHT22

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(RELAY_PIN, GPIO.OUT)

def setRelay(state):
	if state:
		GPIO.output(RELAY_PIN, True)
	else:
		GPIO.output(RELAY_PIN, False)

def getCurrentHumidityTemp():
	return Adafruit_DHT.read_retry(sensor, TEMP_PIN)

def SVP(Tc):
	return 610.7*(10**((7.5*Tc)/(237.3+Tc)))/1000

def VPD(SVP, Rh):
	return (SVP*Rh)/100

def cleanUp():
	GPIO.cleanup()

def main():

	while True:
		currentRh, currentTemp = getCurrentHumidityTemp()
		currentSVP  = SVP(currentTemp)
		currentVPD  = VPD(currentSVP,currentRh)
		VPD1deg     = VPD(SVP(currentTemp-1),100)
		finalVPD    = VPD1deg - currentVPD
		#print time.ctime()
		#print "Rh", currentRh, "Temp", currentTemp, "VPD", currentVPD, "finalVPD", finalVPD

		if finalVPD >= 1:
			setRelay(True)
			#print "LOW Hu on"
		elif finalVPD < 1:
			setRelay(False)
			#print "HIGH Hu off"

		time.sleep(30)

if __name__=="__main__":
	main()
	cleanUp()
