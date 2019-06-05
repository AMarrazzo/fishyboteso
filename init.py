"""Fishy

Usage:
  fishy.py -h | --help
  fishy.py -v | --version
  fishy.py [--debug] [--ip=<ipv4>] [--hook-threshold=<int>] [--check-frequency=<hz>]

Options:
  -h, --help                Show this screen.
  -v, --version             Show version.
  --ip=<ipv4>               Local Ip Address of the android phone.
  --hook-threshold=<int>    Threshold amount for classifier after which label changes [default: 1].
  --check-frequency=<hz>    Sleep after loop in s [default: 1].
  --debug                   Start program in debug controls.
"""

VERSION = "0.1.1"
print("Fishy " + VERSION + " for Elder Scrolls Online")

try:
    from docopt import docopt

    arguments = docopt(__doc__)
    if arguments["--version"]:
        quit()

    print("Loading, Please Wait...")
    import imutils as imutils
    import numpy as np
    from PIL import ImageGrab
    import cv2
    import pyautogui
    import time
    import fishy_network as net
    import pynput
    from pynput.keyboard import Key, Listener
    from decimal import Decimal
    from win32api import GetSystemMetrics
    import pickle
    import win32gui
    import pywintypes
    from abc import ABC, abstractmethod
    from enum import Enum
    import sys
    import numpy as np
    import math
    import pytesseract
    import arrowsAsMouse as arrow
    from threading import Thread
except Exception:
    raise

'''
import stack

fishy
loop
controls
controls_controller
pixel_loc
fishing_event
fishing_mode
fishy_move
window
log
init
'''


class G:
    """
    Initialize global variables
    """
    fishCaught = 0
    stickInitTime = 0
    stop = False
    pause = True
    debug = False

    @staticmethod
    def getControlHelp():
        assert False


"""Helper functions"""


def round_float(v, ndigits=2, rt_str=False):
    d = Decimal(v)
    v_str = ("{0:.%sf}" % ndigits).format(round(d, ndigits))
    if rt_str:
        return v_str
    return Decimal(v_str)


def draw_keypoints(vis, keypoints, color=(0, 0, 255)):
    for kp in keypoints:
        x, y = kp.pt
        cv2.circle(vis, (int(x), int(y)), 5, color, -1)


def bgr2rbg(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


def bgr2hsv(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# np.set_printoptions(threshold=sys.maxsize)
