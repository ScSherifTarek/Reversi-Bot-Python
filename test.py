"""

All coordinates assume a screen resolution of 1280x1024, and Chrome
maximized with the Bookmarks Toolbar enabled.
Down key has been hit 4 times to center play area in browser.
x_pad = 516
y_pad = 277
Play area =  x_pad+1, y_pad+1, 834,595
"""
#Globals
#----------------------------

from PIL import ImageGrab
import PIL.Image
from PIL import Image
import os
import time
import webbrowser
import win32api , win32con
import pyautogui


class Coordinates():
    startBtn=(690, 425)
    playBtn=(683, 590)

def startGame():
    pyautogui.click(Coordinates.startBtn)


def playGame():
    pyautogui.click(Coordinates.playBtn)

def screenGrab():
    x = 526
    y = 275
    step = 40
    box = (x ,y , x+(8*step) , y+(8*step))
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\image' + '.png', 'PNG')

def sendState():
    board =[]
    row = []
    x = 546
    y = 290
    step = 40
    screenGrab()
    ima = Image.open('image.png')
    rgb_im = ima.convert('RGB')
    for i in range(0, 7):
        for j in range(0, 7):
            r, g, b = rgb_im.getpixel(((x+(step*i)), (y+(step*j))))
            if (r==3 and g== 38 and b==68):
                row.append(0)
            elif(r==41 and g==41 and b==41):
                row.append(1)
            elif(r==225 and g==225 and b==225):
                row.append(2)
        board.append(row)
        row = []
    for row in board:
        print(row)
    print("\n")


def calacePosition(first,second):
    x = 546
    y = 290
    step=40
    pyautogui.click(x+(step*first) , y+(step*second))

startGame()
time.sleep(2)
playGame()
time.sleep(2)
playGame()
time.sleep(2)
playGame()
time.sleep(2)
sendState()
time.sleep(2)
calacePosition(4,3)
