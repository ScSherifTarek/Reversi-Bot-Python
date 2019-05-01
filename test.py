"""

All coordinates assume a screen resolution of 1280x1024, and Chrome
maximized with the Bookmarks Toolbar enabled.
Down key has been hit 4 times to center play area in browser.
x_pad = 516
y_pad = 277
Play area =  x_pad+1, y_pad+1, 834,595
"""
# Globals
# ----------------------------

from PIL import ImageGrab
import PIL.Image
from PIL import Image
import os
import time
import webbrowser
import win32api
import win32con
import pyautogui
from config import EMPTYCELL
from config import BLACKCELL
from config import WHITECELL
from state import State
from MovesGenerator import MovesGenerator
from MinimaxAlgorithm import minimax
from StateEvaluator import is_gameover
from StateEvaluator import evaluate


class Coordinates():
    startBtn = (690, 425)
    playBtn = (683, 590)


def startGame():
    pyautogui.click(Coordinates.startBtn)


def playGame():
    pyautogui.click(Coordinates.playBtn)


def screenGrab():
    x = 526
    y = 275
    step = 40
    box = (x, y, x+(8*step), y+(8*step))
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\image' + '.png', 'PNG')


def sendState():
    board = []
    row = []
    x = 546
    y = 290
    step = 40
    screenGrab()
    ima = Image.open('image.png')
    rgb_im = ima.convert('RGB')
    for i in range(0, 7):
        row = []
        for j in range(0, 7):
            r, g, b = rgb_im.getpixel(((x+(step*i)), (y+(step*j))))
            if (r == 3 and g == 38 and b == 68):
                row.append(EMPTYCELL)
            elif(r == 41 and g == 41 and b == 41):
                row.append(BLACKCELL)
            elif(r == 225 and g == 225 and b == 225):
                row.append(WHITECELL)
        board.append(row)

    for row in board:
        print(row)
    print("\n")


def calacePosition(first, second):
    x = 546
    y = 290
    step = 40
    pyautogui.click(x+(step*first), y+(step*second))


startGame()
time.sleep(2)
playGame()
time.sleep(2)
playGame()
time.sleep(2)
playGame()

while(True):
    time.sleep(6)
    state = State(sendState(), WHITECELL)
    state = minimax(state)
    calacePosition(state[0].x, state[0].y)
