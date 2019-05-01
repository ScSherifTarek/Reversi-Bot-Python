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
import os
import time
import webbrowser
import win32api , win32con
import pyautogui
x_pad = 516
y_pad = 277

class Coordinates():
    startBtn=(690, 425)
    playBtn=(683, 609)

def startGame():
    pyautogui.click(Coordinates.startBtn)


def playGame():
    pyautogui.click(Coordinates.playBtn)

startGame()
time.sleep(2)
playGame()
PlayGame()
