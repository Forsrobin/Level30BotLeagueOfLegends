import win32gui
import time
import pyscreenshot as ImageGrab
import cv2
import numpy as np
from PIL import ImageChops
import keyboard
from pynput.mouse import Button, Controller

leaguePos = (0, 0)
leagueSize = (0, 0)

def callback(hwnd, extra):

    rect = win32gui.GetWindowRect(hwnd)
    x = rect[0]
    y = rect[1]
    w = rect[2] - x
    h = rect[3] - y

    global leaguePos
    global leagueSize 

    if "(TM) Client" in str(win32gui.GetWindowText(hwnd)):
        found = True
        if (w, h) != (0, 0):
            leaguePos = (x, y)
            leagueSize = (w, h)


def getInfo(data):
    
    img = ImageGrab.grab(bbox=(data[0], data[1], data[2], data[3]))
    img = np.array(img)
    height, width, channels = img.shape
    green = 0

    for i in range(img.shape[1]):
        for j in range(img.shape[0]):
            if img[j, i][0] > 50 or img[j, i][1] > 50 or img[j, i][2] > 50:
                green = green + 1
                img[j, i] = [0,255,0]
            else:
                img[j, i] = [0,0,0]

    percent = int(float(green / width) * 100)
    return percent
 
def isDead(champ):
        
    img = ImageGrab.grab(bbox=(champ[0], champ[1], champ[2], champ[3]))
    img = np.array(img)
    height, width, channels = img.shape
    
    if (img[0,0][0] > 0 and img[0][0][1] > 50 and img[0][0][2] > 200) or (img[0,0][0] < 25 and img[0][0][1] < 25 and img[0][0][2] < 25):
        return False
    else:
        return True

def main():

    time.sleep(2)

    mouse = Controller()
    posLoL = win32gui.EnumWindows(callback, None)

    #Check if league client exsists
    while leagueSize[0] > 0 and leagueSize[1] > 0:

        posLoL = win32gui.EnumWindows(callback, None)

        mouse.position = (leagueSize[0] / 2 - 250, leagueSize[1] / 2 + 200)  #Set offset
        keyboard.release("f2")
        keyboard.press("f2")

        mouse.press(Button.right) #Click so I move to the position

        healtMex, healtMey = 680, 1045
        manaMex, manaMey = 680, 1064
        healtAlly1x, healtAlly1y = 1670, 780
        healtAlly2x, healtAlly2y = 1735, 780
        healtAlly3x, healtAlly3y = 1800, 780
        healtAlly4x, healtAlly4y = 1864, 780

        healtMe = [leaguePos[0] + healtMex,  leaguePos[1] + healtMey, leaguePos[0] + healtMex + 416, leaguePos[1] + healtMey + 1]
        manaMe = [leaguePos[0] + manaMex, leaguePos[1] + manaMey, leaguePos[0] + manaMex + 416, leaguePos[1] + manaMey + 1]
        healtAlly1 = [leaguePos[0] + healtAlly1x, leaguePos[1] + healtAlly1y, leaguePos[0] + healtAlly1x + 47, leaguePos[1] + healtAlly1y + 1]
        healtAlly2 = [leaguePos[0] + healtAlly2x, leaguePos[1] + healtAlly2y, leaguePos[0] + healtAlly2x + 47, leaguePos[1] + healtAlly2y + 1]
        healtAlly3 = [leaguePos[0] + healtAlly3x, leaguePos[1] + healtAlly3y, leaguePos[0] + healtAlly3x + 47, leaguePos[1] + healtAlly3y + 1]
        healtAlly4 = [leaguePos[0] + healtAlly4x, leaguePos[1] + healtAlly4y, leaguePos[0] + healtAlly4x + 47, leaguePos[1] + healtAlly4y + 1]

        # # health = getInfo(healtMe)
        # # mana = getInfo(manaMe)

        deathAlly1 = [leaguePos[0] + healtAlly1x, leaguePos[1] + healtAlly1y + 11 , leaguePos[0] + healtAlly1x + 1, leaguePos[1] + healtAlly1y + 1 + 11]
        deathAlly2 = [leaguePos[0] + healtAlly2x, leaguePos[1] + healtAlly2y + 11 , leaguePos[0] + healtAlly2x + 1, leaguePos[1] + healtAlly2y + 1 + 11]
        deathAlly3 = [leaguePos[0] + healtAlly3x, leaguePos[1] + healtAlly3y + 11 , leaguePos[0] + healtAlly3x + 1, leaguePos[1] + healtAlly3y + 1 + 11]
        deathAlly4 = [leaguePos[0] + healtAlly4x, leaguePos[1] + healtAlly4y + 11 , leaguePos[0] + healtAlly4x + 1, leaguePos[1] + healtAlly4y + 1 + 11]

        #Check ally healts

        if not isDead(deathAlly1):
            if getInfo(healtAlly1) < 75:
                print("Healing ally 1")
                mouse.release(Button.right)
                mouse.position = (leagueSize[0] / 2, leagueSize[1] / 2) 
                time.sleep(0.2)
                keyboard.press("s")
                time.sleep(0.2)
                mouse.click(Button.left, 1)
                time.sleep(0.2)
                keyboard.release("s")
        else:
            keyboard.press_and_release("b")

        mouse.position = (leagueSize[0] / 2 - 250, leagueSize[1] / 2 + 200)  #Set offset
        mouse.press(Button.right) #Click so I move to the position
        
        if not isDead(deathAlly4) or not isDead(deathAlly3) or not isDead(deathAlly2) or not isDead(deathAlly1):
            if getInfo(healtAlly1) < 25 or getInfo(healtAlly2) < 25 or getInfo(healtAlly3) < 25 or getInfo(healtAlly4) < 25:
                print("Ulting every champ")
                keyboard.press_and_release("f")
                time.sleep(0.2)

        time.sleep(3)
        mouse.release(Button.right)

        #print(health, mana)
        #print(healthAllyOne, healthAllyTwo, healthAllyThre, healthAllyFour)

    else:
        print("Lol finished, go on to next step")

if __name__ == '__main__':
    main()