from PyQt5.QtWidgets import QLabel, QApplication, QGridLayout, QWidget, QGraphicsOpacityEffect, QShortcut
from PyQt5.QtGui import QPixmap, QKeySequence
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
import sys
import os

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

images_glow = [image0_glow, image1_glow, image2_glow, image3_glow, image4_glow]


class Element(QLabel):
    index = 0

    def __init__(self):
        super(Element, self).__init__()
        self.setPixmap(image0)
    def mousePressEvent(self, event):
        if self.index == 0:
            self.setPixmap(image1)
            self.index = 1
        elif self.index == 1:
            self.setPixmap(image2)
            self.index = 2
        elif self.index == 2:
            self.setPixmap(image3)
            self.index = 3
        elif self.index == 3:
            self.setPixmap(image4)
            self.index = 4
        elif self.index == 4:
            self.setPixmap(image0)
            self.index = 0
    def glow(element_index):
        glow = Fade()
        glow.setPixmap(images_glow[Element.index])
        grid.addWidget(glow, 0, element_index)


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
        self.setGeometry(0, 200, 1920, 220)
        self.setStyleSheet("background: black;")
        self.setLayout(grid)
        self.initUI()
    def initUI(self):
        self.tempo120 = QShortcut(QKeySequence('Ctrl+1'), self)
        print("key")
        self.tempo120.activated.connect(lambda *_: render())
        self.tempo150 = QShortcut(QKeySequence('Ctrl+2'), self)
        self.tempo150.activated.connect(lambda *_: render())
        self.tempo180 = QShortcut(QKeySequence('Ctrl+3'), self)
        self.tempo180.activated.connect(lambda *_: render())


def render():
    duration = 8
    FPS = 30
    for i in range(int(duration * FPS)):       
        if duration == 8:
            if i == 0:
                button0.glow()
            elif i == 30:
                button1.glow()
            elif i == 60:
                button2.glow()
            elif i == 90:
                button3.glow()
            elif i == 120:
                button4.glow()
            elif i == 150:
                button5.glow()
            elif i == 180:
                button6.glow()
            elif i == 210:
                button7.glow()

# main


win = MyWindow()

button0 = Element()
button1 = Element()
button2 = Element()
button3 = Element()
button4 = Element()
button5 = Element()
button6 = Element()
button7 = Element()

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

