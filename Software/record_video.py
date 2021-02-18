from picamera import PiCamera
from time import sleep
from datetime import datetime
import os


FRAMERATE = 5 #fps
WAIT_TIME = 120 #video length
RESOLUTION = (1080,720) #resolution camera v2<
MAIN_SAVE_FOLDER = '/home/pi/Desktop/Time-Lapse/video/' #there will be video and images in the folder
START_DELAY = 2 #delay on the begining
END_DELAY = 2 # delay on the video's end

WAIT_TIME+=0.4 # for right frame count
print('started')
camera = PiCamera()
print('passed')
camera.framerate = FRAMERATE
camera.resolution = RESOLUTION
date = datetime.utcnow().strftime('%Y-%m-%d-%H:%M:%S')

filename = '{}_{}x{}_{}_{}'.format(date,RESOLUTION[0],RESOLUTION[1],FRAMERATE,WAIT_TIME)

camera.start_preview()
camera.rotation = 180 
sleep(START_DELAY)
camera.start_recording('%s%s.h264'%(MAIN_SAVE_FOLDER,filename))
sleep(WAIT_TIME)
camera.stop_recording()
camera.stop_preview()
sleep(END_DELAY)
print('video done')
if os.path.exists('%s%s '%(MAIN_SAVE_FOLDER,filename)) == False:
    os.system('mkdir %s%s '%(MAIN_SAVE_FOLDER,filename))
os.system('ffmpeg -i {}{}.h264 {}{}/frame_%d.png'.format(MAIN_SAVE_FOLDER,filename,MAIN_SAVE_FOLDER,filename))
print('images done')

