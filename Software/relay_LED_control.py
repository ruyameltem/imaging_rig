led1 = 21 #GPIO pin to connect to relay
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(led1, GPIO.OUT)
while True:
    GPIO.output(led1, True)    
    time.sleep(2)
    GPIO.output(led1, False)
    time.sleep(2)
