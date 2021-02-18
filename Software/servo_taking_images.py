import RPi.GPIO as GPIO
import time
from picamera import PiCamera
from datetime import datetime

#camera settings
camera = PiCamera() 
camera.start_preview()
camera.resolution=(3280,2464)

#servo settings
servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # setting pin as 17 and choosing 50Hz PWM

WAIT_TIME = .2
IMAGE_COUNT = 15

p.start(12) #initialising servo

#saving images with time stamp
#the folder should be chosen to save
ts=datetime.utcnow().strftime('%Y-%m-%d-%H:%M:%S.%f')
camera.capture('/home/pi/Desktop/Time-Lapse/test/beforedip'+ts+'.jpg','jpeg',use_video_port =True)


print ("hello about to dip")
time.sleep(1)
p.ChangeDutyCycle(3)

i=0
time.sleep(2)
try:
    while True:
        ts=datetime.utcnow().strftime('%Y-%m-%d-%H:%M:%S.%f')
        camera.capture('/home/pi/Desktop/Time-Lapse/test/'+ts+'.jpg','jpeg',use_video_port =True)
        time.sleep(WAIT_TIME)
        i+=1
        if i>=IMAGE_COUNT:
            break

except KeyboardInterrupt:
    camera.stop_preview()
    sys.exit()


time.sleep(1)

print ("now I'm going back to the top")
time.sleep(1)
p.ChangeDutyCycle(12)
time.sleep(2)

ts=datetime.utcnow().strftime('%Y-%m-%d-%H:%M:%S.%f')
camera.capture('/home/pi/Desktop/Time-Lapse/test/after'+ts+'.jpg','jpeg',use_video_port =True)

camera.stop_preview()


time.sleep(5)
p.stop()
GPIO.cleanup()