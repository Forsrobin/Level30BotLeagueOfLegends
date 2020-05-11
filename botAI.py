import cv2
import os
import numpy as np
from matplotlib import pyplot as plt
import win32api, win32con
import pyscreenshot as ImageGrab
import time
from PIL import ImageChops
from PIL import Image
import pytesseract
import keyboard
from pynput.mouse import Button, Controller

def readConfig():
    f = open("settings/bot.conf", 'r')
    settings = {}
    content = f.read().split()
    for a in content:
        name = a.split("=")[0]
        value = a.split("=")[1]
        settings[name] = value
    return(settings)

def levelUp(config, data):
    if data == 'q':
      print("Pressing q")
      keyboard.press_and_release(config['LEVEL_UP_Q'])
    if data == 'w':
      print("Pressing q")
      keyboard.press_and_release(config['LEVEL_UP_W'])
    if data == 'e':
      print("Pressing q")
      keyboard.press_and_release(config['LEVEL_UP_E'])
    if data == 'r':
      print("Pressing q")
      keyboard.press_and_release(config['LEVEL_UP_R'])

def shopItem(config, data):

    #open shop
    keyboard.press_and_release(config['OPEN_BUY_MENU'])
    time.sleep(0.1)
    keyboard.press_and_release("ctrl+L")
    time.sleep(0.1)
    keyboard.write(data)
    time.sleep(0.2)
    keyboard.press_and_release("enter, enter")
    time.sleep(0.1)
    keyboard.press_and_release(config['OPEN_BUY_MENU'])


def main():

    time.sleep(0.5) #timer 
    #config = readConfig()

    #Level up function
    #levelUp(config, 'r')
    
    #Shop an item in league
    #shopItem(config, "Faerie Charm")

if __name__ == "__main__":
    main()