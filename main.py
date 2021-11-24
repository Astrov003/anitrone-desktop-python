from PIL import ImageGrab
import numpy as np
import cv2
import ctypes
from ctypes.wintypes import HWND, DWORD, RECT

dwmapi = ctypes.WinDLL("dwmapi")

hwnd = 787684    # refer to the other answers on how to find the hwnd of your window

rect = RECT()
DMWA_EXTENDED_FRAME_BOUNDS = 9
dwmapi.DwmGetWindowAttribute(HWND(hwnd), DWORD(DMWA_EXTENDED_FRAME_BOUNDS),
                             ctypes.byref(rect), ctypes.sizeof(rect))

print(rect.left, rect.top, rect.right, rect.bottom)


while True:
    img = ImageGrab.grab(bbox=(rect.left, rect.top, rect.right, rect.bottom))
    img_np = np.array(img)
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    cv2.imshow('Capturer', img_final)
    cv2.waitKey(10)
