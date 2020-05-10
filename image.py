import cv2
import os
import numpy as np
from matplotlib import pyplot as plt
import win32api, win32con
import pyscreenshot as ImageGrab

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

#Take screenshot
im = ImageGrab.grab()
im.save('screenshots/screen.jpg')

img = cv2.imread('screenshots/screen.jpg',0)
img2 = img.copy()
template = cv2.imread('refrences/play.png',0)
w, h = template.shape[::-1]

# All the 6 methods for comparison in a list
meth = 'cv2.TM_CCOEFF'
img = img2.copy()
method = eval(meth)

# Apply template Matching
res = cv2.matchTemplate(img,template,method)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

# If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
    top_left = min_loc
else:
    top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)

cv2.rectangle(img,top_left, bottom_right, 255, 2)

plt.subplot(121),plt.imshow(res,cmap = 'gray')
plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img,cmap = 'gray')
plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
plt.suptitle(meth)

# plt.show()
centerX = int((top_left[0] + bottom_right[0]) / 2)
centerY = int((top_left[1] + bottom_right[1]) / 2)
click(centerX,centerY)


os.remove("screenshots/screen.jpg")