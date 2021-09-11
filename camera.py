from picamera import PiCamera
from time import sleep
from datetime import datetime
#from gpiozero import Button
#from signal import pause

camera = PiCamera()

# 2 buttons connected to GPIO2 / 3 + gnd
#left_button = Button(2)
#right_button = Button(3)

# change save location to USB drive

# take 5 pictures, once every 5s
#camera.resolution = (2592, 1944)
#camera.framerate = 15
#camera.start_preview(alpha=200)
#camera.exposure_mode = 'night'
#for i in range(5):
#    sleep(5)
#    timestamp = datetime.now().isoformat()
#    camera.capture('/home/pi/Desktop/image%s.jpg' % timestamp)
#    OR camera.capture('/home/pi/Desktop/image%s.jpg' % i)
#camera.stop_preview()

#take a 5s video after 5s
camera.resolution = (1920, 1080)
camera.framerate = 15
camera.start_preview(alpha=200)
camera.exposure_mode = 'auto'
sleep(5)
timestamp = datetime.now().isoformat()
camera.start_recording('/home/pi/Desktop/video%s.h264' % timestamp)
sleep(5)
camera.stop_recording()
camera.stop_preview()


# unmount USB drive
cmd = "sudo umount /dev/sdb1"
os.system(cmd)


# take a picture when (R) button is pushed

#def capture():
#    timestamp = datetime.now().isoformat()
#    camera.capture('/home/pi/%s.jpg' % timestamp)
#right_button.when_pressed = capture
#pause()

# L button starts preview, R captures

#def capture():
#    timestamp = datetime.now().isoformat()
#    camera.capture('/home/pi/%s.jpg' % timestamp)
#left_button.when_pressed = camera.start_preview
#left_button.when_released = camera.stop_preview
#right_button.when_pressed = capture
#pause()