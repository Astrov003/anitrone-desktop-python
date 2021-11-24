from win32gui import FindWindow, GetWindowRect
from PIL import ImageGrab
import numpy as np
import cv2

# Find the position of the app on screen
window_handle = FindWindow(None, "Anitrone")
window_rect = GetWindowRect(window_handle)
print(window_rect)

while True:
    img = ImageGrab.grab(bbox=(window_rect))
    img_np = np.array(img)
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    cv2.imshow('Capturer', img_final)
    cv2.waitKey(10)