import RPi.GPIO as GPIO
from time import sleep
from picamera import PiCamera
from datetime import datetime
import io
import time 
from PIL import Image,ImageFile 
#import height_calculator as hc
import threading 

class create_before (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self): 
      record() 
      
class create_after (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
       after_record()


names = []

#the second takes for from servo's starting going down and experiement's ending
EXPERIMENT_TIME = 8

#servo step count
DISTANCE = 12

#servo movement
IS_SERVO_MOVED = 2

#servo downtime
SERVO_DOWN_TIME = DISTANCE + IS_SERVO_MOVED

#maximum resolution
RESOLUTION = (3280,2464)

#maximum picture
FPS = 10

#picture count
IMAGE_COUNT = FPS * (EXPERIMENT_TIME + SERVO_DOWN_TIME)

def outputs():
    global names, IMAGE_COUNT
    
    stream = io.BytesIO()
    
    for i in range(IMAGE_COUNT) : 
        # This returns the stream for the camera to capture to
        yield stream
        stream.seek(0)
        names.append([datetime.utcnow().strftime('%Y-%m-%d-%H:%M:%S.%f'),stream.getvalue()])
        # Once the capture is complete, the loop continues here
        # (read up on generator functions in Python to understand
        # the yield statement). Here you could do some processing
        # on the image...
        #stream.seek(0)
        #img = Image.open(stream)
        # Finally, reset the stream for the next capture
        stream.truncate()
        print('image',i,datetime.utcnow().strftime('%Y-%m-%d-%H:%M:%S.%f')) 
    

def record():
    global RESOLUTION,FPS

    print("LED is about to open")
    #LED will be open
    led1 = 21 #GPIO pin to connect to relay
    
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led1, GPIO.OUT)

    GPIO.output(led1, True)    
    time.sleep(1)
    
    print('taking pictures')
    
    camera = PiCamera() 
    camera.start_preview()
    #start capture     
    camera.resolution=RESOLUTION
    camera.framerate = FPS
    camera.rotation = 180
    
    camera.capture_sequence(outputs(), 'jpeg', use_video_port=True)
    #Experiment ended stop the camera
    camera.stop_preview()
    print('capturing ended')

    #LED is stopping
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led1, GPIO.OUT)
    GPIO.output(led1, False)
    time.sleep(2)
    print('LED stopped')

    #Start the calculation

    i=1
    results = []

    #change this settings according to the environment

    ENV_RED = 75
    ENV_COLORS = 75
    ENV_STABILITY = 20

    #calculate heights for every picture

    print('calculating started')
      
    i=0
    for frameData in names:
        byteImg = frameData[1]
        byteImg = io.BytesIO(byteImg)
        byteImg = Image.open(byteImg) 
        filename = "/home/pi/Desktop/Time-Lapse/test/" + frameData[0] + ".jpeg"
        byteImg.save(filename, 'JPEG')
        print('saving photo',i)
        i+=1
        '''
        try:
            results.append(hc.main(ENV_RED,ENV_COLORS,ENV_STABILITY,byteImg))
        except:
            print("error happened on :",
                  "image_number = "+str(i),
                  "image_name = "+frameData[0])
            continue
            
        print('calculated',i)
        i+=1
        '''

    #save the results

    '''
    with file as open('/home/pi/Desktop/Time-Lapse/test/'+datetime.utcnow().strftime('%Y-%m-%d-%H:%M:%S.%f')+'.txt','w'):
        file.write(results)
    '''
 

def after_record():
    global DISTANCE,IS_SERVO_MOVED,EXPERIMENT_TIME
        
    servoPIN = 17
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPIN, GPIO.OUT)

    p = GPIO.PWM(servoPIN, 50) # setting pin as 17 and choosing 50Hz PWM
    duty = 0

    #initialising servo
    p.start(duty)
    duty  = 12
    while 0 < duty:
        duty-=3
        p.ChangeDutyCycle(duty)
        sleep(0.1)
        
    #preparing
    sleep(4)
    
    print('servo to down')
    #servo to down 
    while duty < DISTANCE:
        duty+=1
        p.ChangeDutyCycle(duty) 
                 
    sleep(IS_SERVO_MOVED-1.5)
    p.stop()

    print('servo on down')

    #Experiment started
    sleep(EXPERIMENT_TIME)
    
    print('servo to top')
    p.start(duty)    
    #servo to top
    while 0 < duty:
        duty-=3
        p.ChangeDutyCycle(duty)
        sleep(0.1)
    sleep(IS_SERVO_MOVED)
    p.stop()

    #is servo on top
    sleep(IS_SERVO_MOVED)

    print('servo on top')

    #stop the servo
    p.stop()

     
thread1 = create_before(1,'1',1)
thread2 = create_after(2,'2',2)

thread1.start()
thread2.start()
