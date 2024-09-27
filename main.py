from PyQt5.QtWidgets import QLabel, QApplication, QGridLayout, QWidget, QGraphicsOpacityEffect, QShortcut
from PyQt5.QtGui import QPixmap, QKeySequence
from PyQt5.QtCore import Qt, QObject, QThread, pyqtSignal
from PyQt5 import QtCore
import sys
import os

# Render imports
from PIL import ImageGrab
import numpy as np
import cv2
import ctypes
from ctypes.wintypes import HWND, DWORD, RECT
import pywintypes
from win32 import win32gui
import datetime

from app.framer import frame_animation

ATTACK = 200
HOLD = ATTACK + 0 # delays release from the beggining of attack, hence attack + additional time 
RELEASE = 1700
FADE_RANGE = 1


# fix menu path when compiling to one file
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


app = QApplication(sys.argv)
grid = QGridLayout()


# Load sprite images
images = [
    QPixmap(resource_path(f'images/sprite_{i}.png')).scaled(220, 220, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
    for i in range(6)
]

# Glow images
images_glow = [
    QPixmap(resource_path(f'images/sprite_{i}_glow.png')).scaled(220, 220, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
    for i in range(6)
]

class Element(QLabel):
    # Signal to notify the window whenever the imgIndex changes
    indexChanged = pyqtSignal(int, int)

    def __init__(self, elementIndex):
        super(Element, self).__init__()
        self.elementIndex = elementIndex
        self.imgIndex = 0  # Instance variable to track the image index
        self.setPixmap(images[0])
        self.updatePixmap()

    def mousePressEvent(self, event):
        # Update the imgIndex on click
        self.imgIndex = (self.imgIndex + 1) % len(images)
        self.updatePixmap()

        # Emit signal that the imgIndex has changed
        self.indexChanged.emit(self.elementIndex, self.imgIndex)

    def updatePixmap(self):
        # Update the pixmap of the QLabel based on imgIndex
        self.setPixmap(images[self.imgIndex])

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle('Anitrone')
        self.setGeometry(0, 200, 1920, 220)
        self.setStyleSheet("background: black;")

        # Layout and element tracking
        grid = QGridLayout(self)
        self.elements = [Element(i) for i in range(8)]
        self.elementStates = [0] * len(self.elements)  # Track imgIndex of each element

        # Connect each element's indexChanged signal to the state handler
        for i, element in enumerate(self.elements):
            element.indexChanged.connect(self.updateElementState)
            grid.addWidget(element, 0, i)

        self.keyStroke()

    def keyStroke(self):
        self.tempo120 = QShortcut(QKeySequence('Ctrl+1'), self)
        self.tempo120.activated.connect(lambda: self.start(120))
        self.tempo150 = QShortcut(QKeySequence('Ctrl+2'), self)
        self.tempo150.activated.connect(lambda: self.start(150))
        self.tempo180 = QShortcut(QKeySequence('Ctrl+3'), self)
        self.tempo180.activated.connect(lambda: self.start(180))

    def updateElementState(self, elementIndex, imgIndex):
        # Update the internal state of elements whenever an imgIndex changes
        self.elementStates[elementIndex] = imgIndex

    def start(self, tempo):
        # Directly use the stored imgIndex values for each element
        frame_animation(tempo, self.elementStates)  # Use the updated element states here

        


# main
win = MyWindow()

button0 = Element(0)
button1 = Element(1)
button2 = Element(2)
button3 = Element(3)
button4 = Element(4)
button5 = Element(5)
button6 = Element(6)
button7 = Element(7)

grid.addWidget(button0, 0, 0)
grid.addWidget(button1, 0, 1)
grid.addWidget(button2, 0, 2)
grid.addWidget(button3, 0, 3)
grid.addWidget(button4, 0, 4)
grid.addWidget(button5, 0, 5)
grid.addWidget(button6, 0, 6)
grid.addWidget(button7, 0, 7)

win.show()
sys.exit(app.exec_())