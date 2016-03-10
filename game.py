from glob import glob
import random
import os

WIDTH = 1600
HEIGHT = 900

def sanitise(f):
    return f.replace('images/', '').replace('.jpg', '')

images = [sanitise(f) for f in glob("images/*.jpg")]

n = 0
alpha = 200

def draw():
    screen.blit(images[n], (0, 0))

def on_key_down(key):
    global n
    global alpha
    if key == keys.RIGHT:
        n += 1
        screen.blit(images[n], (0, 0))
    elif key == keys.LEFT:
        n -= 1
        screen.blit(images[n], (0, 0))
    elif key == keys.UP:
        alpha += 20
        os.system("omxplayer /opt/vc/src/hello_pi/hello_video/test.h264 --alpha %i" % alpha)
    elif key == keys.DOWN:
        alpha -= 20
        os.system("omxplayer /opt/vc/src/hello_pi/hello_video/test.h264 --alpha %i" % alpha)
    
        
