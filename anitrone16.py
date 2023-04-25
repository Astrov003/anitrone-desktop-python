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


image0 = QPixmap(resource_path('images/dot.png'))
image0 = image0.scaledToWidth(220, Qt.SmoothTransformation)
image0 = image0.scaledToHeight(220, Qt.SmoothTransformation)
image1 = QPixmap(resource_path('images/down_full.png'))
image1 = image1.scaledToWidth(220, Qt.SmoothTransformation)
image1 = image1.scaledToHeight(220, Qt.SmoothTransformation)
image2 = QPixmap(resource_path('images/down_open.png'))
image2 = image2.scaledToWidth(220, Qt.SmoothTransformation)
image2 = image2.scaledToHeight(220, Qt.SmoothTransformation)
image3 = QPixmap(resource_path('images/up_full.png'))
image3 = image3.scaledToWidth(220, Qt.SmoothTransformation)
image3 = image3.scaledToHeight(220, Qt.SmoothTransformation)
image4 = QPixmap(resource_path('images/up_open.png'))
image4 = image4.scaledToWidth(220, Qt.SmoothTransformation)
image4 = image4.scaledToHeight(220, Qt.SmoothTransformation)
image5 = QPixmap(resource_path('images/cross.png'))
image5 = image5.scaledToWidth(220, Qt.SmoothTransformation)
image5 = image5.scaledToHeight(220, Qt.SmoothTransformation)

image0_glow = QPixmap(resource_path('images/dot_glow.png'))
image0_glow = image0_glow.scaledToWidth(220, Qt.SmoothTransformation)
image0_glow = image0_glow.scaledToHeight(220, Qt.SmoothTransformation)
image1_glow = QPixmap(resource_path('images/down_full_glow.png'))
image1_glow = image1_glow .scaledToWidth(220, Qt.SmoothTransformation)
image1_glow = image1_glow .scaledToHeight(220, Qt.SmoothTransformation)
image2_glow = QPixmap(resource_path('images/down_open_glow.png'))
image2_glow = image2_glow .scaledToWidth(220, Qt.SmoothTransformation)
image2_glow = image2_glow .scaledToHeight(220, Qt.SmoothTransformation)
image3_glow = QPixmap(resource_path('images/up_full_glow.png'))
image3_glow = image3_glow .scaledToWidth(220, Qt.SmoothTransformation)
image3_glow = image3_glow .scaledToHeight(220, Qt.SmoothTransformation)
image4_glow = QPixmap(resource_path('images/up_open_glow.png'))
image4_glow = image4_glow .scaledToWidth(220, Qt.SmoothTransformation)
image4_glow = image4_glow .scaledToHeight(220, Qt.SmoothTransformation)
image5_glow = QPixmap(resource_path('images/cross_glow.png'))
image5_glow = image5_glow .scaledToWidth(220, Qt.SmoothTransformation)
image5_glow = image5_glow .scaledToHeight(220, Qt.SmoothTransformation)

images_glow = [image0_glow, image1_glow, image2_glow, image3_glow, image4_glow, image5_glow]

class Element(QLabel):
    imgIndex = 0
    elementIndex = 0

    def __init__(self, elementRow, elementIndex):
        super(Element, self).__init__()
        self.elementIndex = elementIndex
        self.elementRow = elementRow
        self.setPixmap(image0)
    def mousePressEvent(self, event):
        if self.imgIndex == 0:
            self.setPixmap(image1)
            self.imgIndex = 1
        elif self.imgIndex == 1:
            self.setPixmap(image2)
            self.imgIndex = 2
        elif self.imgIndex == 2:
            self.setPixmap(image3)
            self.imgIndex = 3
        elif self.imgIndex == 3:
            self.setPixmap(image4)
            self.imgIndex = 4
        elif self.imgIndex == 4:
            self.setPixmap(image5)
            self.imgIndex = 5
        elif self.imgIndex == 5:
            self.setPixmap(image0)
            self.imgIndex = 0
    def glow(self):
        glow = Fade()
        glow.setPixmap(images_glow[self.imgIndex])
        grid.addWidget(glow, self.elementRow, self.elementIndex)


class Fade(QLabel):
    def __init__(self):
        super().__init__()
        self.fadeIn()
        QtCore.QTimer.singleShot(HOLD, lambda:self.fadeOut())
    def fadeIn(self):   
        self.effect = QGraphicsOpacityEffect()
        self.setGraphicsEffect(self.effect)
        self.animation = QtCore.QPropertyAnimation(self.effect, b"opacity")
        self.animation.setDuration(ATTACK)
        self.animation.setStartValue(0)
        self.animation.setEndValue(FADE_RANGE)
        self.animation.start()
    def fadeOut(self):
        self.effect = QGraphicsOpacityEffect()
        self.setGraphicsEffect(self.effect)
        self.animation = QtCore.QPropertyAnimation(self.effect, b"opacity")
        self.animation.setDuration(RELEASE)
        self.animation.setStartValue(FADE_RANGE)
        self.animation.setEndValue(0)
        self.animation.start()


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle('Anitrone')
        self.setGeometry(0, 200, 1920, 440)
        self.setStyleSheet("background: black;")
        self.setLayout(grid)
        self.keyStroke()
    def keyStroke(self):
        self.tempo120 = QShortcut(QKeySequence('Ctrl+1'), self)
        self.tempo120.activated.connect(lambda *_: self.start(120))
        self.tempo150 = QShortcut(QKeySequence('Ctrl+2'), self)
        self.tempo150.activated.connect(lambda *_: self.start(150))
        self.tempo180 = QShortcut(QKeySequence('Ctrl+3'), self)
        self.tempo180.activated.connect(lambda *_: self.start(180))

    tempo = 0
    def start(self, tempo):
        MyWindow.tempo = tempo

        # Create a QThread object
        self.thread = QThread()
        # Create a worker object
        self.worker = Render()
        # Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Connect signals and slots
        self.thread.started.connect(self.worker.render)
        
        self.worker.glow0.connect(button0.glow)
        self.worker.glow1.connect(button1.glow)
        self.worker.glow2.connect(button2.glow)
        self.worker.glow3.connect(button3.glow)
        self.worker.glow4.connect(button4.glow)
        self.worker.glow5.connect(button5.glow)
        self.worker.glow6.connect(button6.glow)
        self.worker.glow7.connect(button7.glow)
        self.worker.glow8.connect(button8.glow)
        self.worker.glow9.connect(button9.glow)
        self.worker.glow10.connect(button10.glow)
        self.worker.glow11.connect(button11.glow)
        self.worker.glow12.connect(button12.glow)
        self.worker.glow13.connect(button13.glow)
        self.worker.glow14.connect(button14.glow)
        self.worker.glow15.connect(button15.glow)

        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.worker.finished.connect(self.thread.deleteLater)
        # Start the thread
        self.thread.start()


class Render(QObject):
    finished = pyqtSignal()
    glow0 = pyqtSignal()
    glow1 = pyqtSignal()
    glow2 = pyqtSignal()
    glow3 = pyqtSignal()
    glow4 = pyqtSignal()
    glow5 = pyqtSignal()
    glow6 = pyqtSignal()
    glow7 = pyqtSignal()
    glow8 = pyqtSignal()
    glow9 = pyqtSignal()
    glow10 = pyqtSignal()
    glow11 = pyqtSignal()
    glow12 = pyqtSignal()
    glow13 = pyqtSignal()
    glow14 = pyqtSignal()
    glow15 = pyqtSignal()

    def render(self):
        # Getting app window position
        dwmapi = ctypes.WinDLL("dwmapi")
        hwnd = win32gui.FindWindow(None, 'Anitrone')
        rect = RECT()
        DMWA_EXTENDED_FRAME_BOUNDS = 9
        dwmapi.DwmGetWindowAttribute(HWND(hwnd), DWORD(DMWA_EXTENDED_FRAME_BOUNDS), ctypes.byref(rect), ctypes.sizeof(rect))

        FPS = 30
        time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        file_name = f'{time_stamp}.avi'
        fourcc = cv2.VideoWriter_fourcc(*'FFV1')
        captured_video = cv2.VideoWriter(file_name, fourcc, FPS, (rect.right-rect.left, rect.bottom-rect.top-34))
        
        if MyWindow.tempo == 120:
            duration = 16
        elif MyWindow.tempo == 150:
            duration = 12.8
        elif MyWindow.tempo == 180:
            duration = 10.7

        for i in range(int(duration * FPS)):
            img = ImageGrab.grab(bbox=(rect.left, rect.top+32, rect.right, rect.bottom-2))
            img_np = np.array(img)
            img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

            if duration == 16:
                if i == 0:
                    self.glow0.emit()
                elif i == 30:
                    self.glow1.emit()
                elif i == 60:
                    self.glow2.emit()
                elif i == 90:
                    self.glow3.emit()
                elif i == 120:
                    self.glow4.emit()
                elif i == 150:
                    self.glow5.emit()
                elif i == 180:
                    self.glow6.emit()
                elif i == 210:
                    self.glow7.emit()
                elif i == 240:
                    self.glow8.emit()
                elif i == 270:
                    self.glow9.emit()
                elif i == 300:
                    self.glow10.emit()
                elif i == 330:
                    self.glow11.emit()
                elif i == 360:
                    self.glow12.emit()
                elif i == 390:
                    self.glow13.emit()
                elif i == 420:
                    self.glow14.emit()
                elif i == 450:
                    self.glow15.emit()
            elif duration == 6.4:
                if i == 0:
                    self.glow0.emit()
                elif i == 24:
                    self.glow1.emit()
                elif i == 48:
                    self.glow2.emit()
                elif i == 72:
                    self.glow3.emit()
                elif i == 96:
                    self.glow4.emit()
                elif i == 120:
                    self.glow5.emit()
                elif i == 144:
                    self.glow6.emit()
                elif i == 168:
                    self.glow7.emit()
                elif i == 192:
                    self.glow0.emit()
                elif i == 216:
                    self.glow1.emit()
                elif i == 240:
                    self.glow2.emit()
                elif i == 264:
                    self.glow3.emit()
                elif i == 288:
                    self.glow4.emit()
                elif i == 312:
                    self.glow5.emit()
                elif i == 336:
                    self.glow6.emit()
                elif i == 360:
                    self.glow7.emit()
            elif duration == 5.35:
                if i == 0:
                    self.glow0.emit()
                elif i == 20:
                    self.glow1.emit()
                elif i == 40:
                    self.glow2.emit()
                elif i == 60:
                    self.glow3.emit()
                elif i == 80:
                    self.glow4.emit()
                elif i == 100:
                    self.glow5.emit()
                elif i == 120:
                    self.glow6.emit()
                elif i == 140:
                    self.glow7.emit()
                elif i == 160:
                    self.glow0.emit()
                elif i == 180:
                    self.glow1.emit()
                elif i == 200:
                    self.glow2.emit()
                elif i == 220:
                    self.glow3.emit()
                elif i == 240:
                    self.glow4.emit()
                elif i == 260:
                    self.glow5.emit()
                elif i == 280:
                    self.glow6.emit()
                elif i == 300:
                    self.glow7.emit()

            captured_video.write(img_final)

        cv2.destroyAllWindows()
        captured_video.release()
        self.finished.emit()


# main
win = MyWindow()

button0 = Element(0, 0)
button1 = Element(0, 1)
button2 = Element(0, 2)
button3 = Element(0, 3)
button4 = Element(0, 4)
button5 = Element(0, 5)
button6 = Element(0, 6)
button7 = Element(0, 7)
button8 = Element(1, 0)
button9 = Element(1, 1)
button10 = Element(1, 2)
button11 = Element(1, 3)
button12 = Element(1, 4)
button13 = Element(1, 5)
button14 = Element(1, 6)
button15 = Element(1, 7)

grid.addWidget(button0, 0, 0)
grid.addWidget(button1, 0, 1)
grid.addWidget(button2, 0, 2)
grid.addWidget(button3, 0, 3)
grid.addWidget(button4, 0, 4)
grid.addWidget(button5, 0, 5)
grid.addWidget(button6, 0, 6)
grid.addWidget(button7, 0, 7)
grid.addWidget(button8, 1, 0)
grid.addWidget(button9, 1, 1)
grid.addWidget(button10, 1, 2)
grid.addWidget(button11, 1, 3)
grid.addWidget(button12, 1, 4)
grid.addWidget(button13, 1, 5)
grid.addWidget(button14, 1, 6)
grid.addWidget(button15, 1, 7)

win.show()
sys.exit(app.exec_())