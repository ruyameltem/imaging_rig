from picamera import PiCamera
from time import sleep
import time
from datetime import datetime

WAIT_TIME = 1 # between 0 and 100

camera = PiCamera()

camera.start_preview()
camera.rotation = 180 # 90 derece cevir
camera.resolution = (3280,2464) #2028,1520
#camera.brightness = 60 # between 0 and 100
#camera.image_effect = 'colorpoint'# none, negative, solarize, sketch, denoise
# you can also use effects: emboss, oilpaint, hatch, gpen, pastel, watercolor
# film, blur, saturation, washedout, posterise, colorpoint, colorbalance
# cartoon, deinterlace1, deinterlace2, colorswap
#camera.awb_mode = 'fluorescent'
#are available have these settings in brackets
#off, auto, sun, cloud, shade, tungsten, fluorescent
#incandescent, flash, horizon, greyworld
camera.iso = 300 # iso length 100 - 800
#camera.exposure_mode = 'verylong'
#fast-moving objects need a short, low-light needs a long exp. time
# off, auto, night, nightpreview, backlight, fireworks,beach
# spotlight, sports, snow, verylong, fixedfps, antishake,
#camera.resolution = (2592,1944) #1020, 768
#The maximum resolution is 2592×1944 for still photos,
#and 1920×1080 for video recording.
try:
    while True:
        ts=datetime.utcnow().strftime('%Y-%m-%d-%H:%M:%S:%f')
        camera.capture('/home/pi/Desktop/Time-Lapse/img-'+ts+'.jpg')
        time.sleep(WAIT_TIME)
    
except KeyboardInterrupt:
    camera.stop_preview()
    sys.exit()
        
camera.stop_preview()

