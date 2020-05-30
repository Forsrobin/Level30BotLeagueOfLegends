import cv2
import os
import numpy as np
from matplotlib import pyplot as plt
import win32api, win32con
import pytesseract
import pyscreenshot as ImageGrab
import time
from PIL import ImageChops
from PIL import Image
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

def decideItem(itemToBuy, inventory):

    #Check if I have the items in my inventory, if not proced to buy all components
    buyItem = None


    for item in itemToBuy:
        #Check if item is list
        if type(item) == list:
            buyItem = decideItem(item, inventory)

        #If item is not a list that means that it's and core item
        else:
            if item not in inventory:
                return(item)
                #return item

def shopItem(config, data, inventory):

    itemToBuy = data

    recipies = [
      [ [ ['Null-Magic Mantle'] , ['Cloth Armor'] , 'Aegis of the Legion' ] , [ 'Null-Magic Mantle' ] , 'Locket of the Iron Solari']
    ]

    #Check if item is a recipie
    for e,a in enumerate(recipies):
        if itemToBuy in a:
            itemToBuy = decideItem(recipies[e], inventory)

    print(itemToBuy)

    #open shop
    # im = ImageGrab.grab(bbox=(1131,945,1131 + 140,945 + 90))
    # img = np.array(im)

    # keyboard.press_and_release(config['OPEN_BUY_MENU'])
    # time.sleep(0.1)
    # keyboard.press_and_release("ctrl+L")
    # time.sleep(0.1)
    # keyboard.write(itemToBuy)
    # time.sleep(0.2)
    # keyboard.press_and_release("enter, enter")
    # time.sleep(0.1)
    # keyboard.press_and_release('esc')
    # time.sleep(0.1)

    # diff = ImageChops.difference(ImageGrab.grab(bbox=(1131,945,1131 + 140,945 + 90)), im)
    # bbox = diff.getbbox()

    # if bbox is not None: # exact comparison
    #     print("Bought item")
    #     inventory.append(itemToBuy)



def getGold():
    kernel = np.ones((1, 1), np.uint8)
    pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
    im = ImageGrab.grab(bbox=(690,875,690 + 150,875 + 50))
    img = np.array(im)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gold = pytesseract.image_to_string(img, config='digits') 
    print(gold)

def main():

    inventory = ['Cloth Armor', 'Null-Magic Mantle']

    time.sleep(0.5) #timer 
    config = readConfig()

    #Level up function
    #levelUp(config, 'r')
    
    #Shop an item in league
    #gold = getGold()

    # shopItem(config, "Faerie Charm", inventory)
    time.sleep(0.1)
    shopItem(config, "Locket of the Iron Solari", inventory)

if __name__ == "__main__":
    main()