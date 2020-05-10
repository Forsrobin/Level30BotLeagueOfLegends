import cv2
import os
import numpy as np
from matplotlib import pyplot as plt
import win32api, win32con
import pyscreenshot as ImageGrab
import time
from PIL import ImageChops

def findCordinates(data):
    img = cv2.imread('screenshots/screen.jpg',0)
    img2 = img.copy()
    template = cv2.imread('refrences/'+data,0)
    w, h = template.shape[::-1]

    # All the 6 methods for comparison in a list
    meth = 'cv2.TM_CCOEFF_NORMED'
    img = img2.copy()
    method = eval(meth)

    # Apply template Matching
    res = cv2.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    centerX = int((top_left[0] + bottom_right[0]) / 2)
    centerY = int((top_left[1] + bottom_right[1]) / 2)
    return (centerX,centerY)

def capture(data):
    if data == 'add':
        im = ImageGrab.grab()
        im.save('screenshots/screen.jpg')
    elif data == 'remove':
        os.remove("screenshots/screen.jpg")

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def clickElement(data):
    capture('add')
    cordinates = findCordinates(data+'.png')
    click(cordinates[0], cordinates[1])

def findElement(data):
    capture('add')
    cordinates = findCordinates(data+'.png')

    return cordinates

def champSelect():

    clickElement('supporticon')
    clickElement('soraka')
    clickElement('lockin')

    print("Done")
    input()

def detectChangeOnScreen():
    im = ImageGrab.grab(bbox=(50,50,100,100))
    while True:
        diff = ImageChops.difference(ImageGrab.grab(bbox=(50,50,500,500)), im)
        bbox = diff.getbbox()
        if bbox is not None: # exact comparison
            break

    return True

def cgangeScreen():
    screenchanged = False
    while screenchanged == False:
        screenchanged = detectChangeOnScreen()

    print("Screen Changed, Continue to next task")
    return

def startGame():

    matchfound = False
    cords = ()

    #Click play button
    clickElement('play')
    time.sleep(1)
    clickElement('coop')
    time.sleep(1)
    clickElement('intermediate')
    time.sleep(1)
    clickElement('confirm')
    time.sleep(3)
    clickElement('findmatch')
    cords = findElement('accept')
    time.sleep(2)
    while matchfound == False:
        tmpcords = findElement('decline')
        if tmpcords != cords:
            click(tmpcords[0], tmpcords[1])
            matchfound = True;
        time.sleep(1)
        
    print("Done")
    input()