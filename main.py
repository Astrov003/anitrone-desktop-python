import sys
from PyQt5.QtWidgets import QApplication, QGridLayout, QWidget, QLabel, QGraphicsOpacityEffect, QShortcut
from PyQt5.QtGui import QPixmap, QKeySequence
from PyQt5 import QtCore, QtTest
import time
#from PyQt5.QtCore import Qt, pyqtSignal, QRect
#from PyQt5.QtCore import QPropertyAnimation


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle('Anitrone')
        self.setGeometry(200, 200, 820, 120)
        self.setStyleSheet("background: black;")
        self.setLayout(grid)
        self.initUI()

    def initUI(self):
        self.msgSc = QShortcut(QKeySequence('Ctrl+1'), self)
        self.msgSc.activated.connect(lambda *_: trigger_glow())
    

# INIT BUTTONS + CLICK DEFINED

class Image0(QLabel):
    def mousePressEvent(self, event):
        print ("clicked0")
        btn0.setPixmap(image1)

class Image1(QLabel):     
    def mousePressEvent(self, event):
        print ("clicked1")

class Image2(QLabel):     
    def mousePressEvent(self, event):
        print ("clicked2")

class Image3(QLabel):     
    def mousePressEvent(self, event):
        print ("clicked3")

class Image4(QLabel):     
    def mousePressEvent(self, event):
        print ("clicked4")

class Image5(QLabel):     
    def mousePressEvent(self, event):
        print ("clicked5")

class Image6(QLabel):     
    def mousePressEvent(self, event):
        print ("clicked6")

class Image7(QLabel):     
    def mousePressEvent(self, event):
        print ("clicked7")


# FADE IN IMAGES

class FadeInImage0(QLabel):
    def __init__(self):
        super().__init__()
        self.fadeIn()
        QtCore.QTimer.singleShot(1000, lambda:self.fadeOut())
    def fadeIn(self):   
        self.effect = QGraphicsOpacityEffect()
        self.setGraphicsEffect(self.effect)
        self.animation = QtCore.QPropertyAnimation(self.effect, b"opacity")
        self.animation.setDuration(1000)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()
    def fadeOut(self):
        self.effect = QGraphicsOpacityEffect()
        self.setGraphicsEffect(self.effect)
        self.animation = QtCore.QPropertyAnimation(self.effect, b"opacity")
        self.animation.setDuration(1000)
        self.animation.setStartValue(1)
        self.animation.setEndValue(0)
        self.animation.start()


def trigger_glow():
    global btn0_image
    if btn0_image == 0:
        image0_glow = QPixmap('./images/dot_glow.png')
        image0_glow = image0_glow.scaledToWidth(120)
        image0_glow = image0_glow.scaledToHeight(120)
        img0_glow = FadeInImage0()
        img0_glow.setPixmap(image0_glow)
        grid.addWidget(img0_glow, 0, 0)
        
        
    

#==== GLOBAL VARIABLES====

btn0_image = 0
btn1_image = 0
btn2_image = 0
btn3_image = 0
btn4_image = 0
btn5_image = 0
btn6_image = 0
btn7_image = 0

#==== MAIN ================

app = QApplication(sys.argv)
grid = QGridLayout()

win = MyWindow()

# BUTTONS

button0 = QPixmap('./images/dot.png')
button0 = button0.scaledToWidth(120)
button0 = button0.scaledToHeight(120)

btn0 = Image0()
btn0.setPixmap(button0)


btn1 = Image1()
btn1.setPixmap(button0)
btn2 = Image2()
btn2.setPixmap(button0)
btn3 = Image3()
btn3.setPixmap(button0)
btn4 = Image4()
btn4.setPixmap(button0)
btn5 = Image5()
btn5.setPixmap(button0)
btn6 = Image6()
btn6.setPixmap(button0)
btn7 = Image7()
btn7.setPixmap(button0)


### BASE IMAGES

image0 = QPixmap('./images/dot.png')
image0 = image0.scaledToWidth(120)
image0 = image0.scaledToHeight(120)
img0 = QLabel()
img0.setPixmap(image0)
image1 = QPixmap('./images/down_full.png')
image1 = image1.scaledToWidth(120)
image1 = image1.scaledToHeight(120)
img1 = QLabel()
img1.setPixmap(image1)
image2 = QPixmap('./images/down_open.png')
image2 = image2.scaledToWidth(120)
image2 = image2.scaledToHeight(120)
img2 = QLabel()
img2.setPixmap(image2)
image3 = QPixmap('./images/up_full.png')
image3 = image3.scaledToWidth(120)
image3 = image3.scaledToHeight(120)
img3 = QLabel()
img3.setPixmap(image3)
image4 = QPixmap('./images/up_open.png')
image4 = image4.scaledToWidth(120)
image4 = image4.scaledToHeight(120)
img4 = QLabel()
img4.setPixmap(image4)


images = [img0, img1, img2, img3, img4]

### GLOW IMAGES




image1_glow = QPixmap('./images/down_full_glow.png')
image1_glow = image1_glow .scaledToWidth(120)
image1_glow = image1_glow .scaledToHeight(120)
img1_glow= QLabel()
img1_glow.setPixmap(image1_glow)
image2_glow = QPixmap('./images/down_open_glow.png')
image2_glow = image2_glow .scaledToWidth(120)
image2_glow = image2_glow .scaledToHeight(120)
img2_glow = QLabel()
img2_glow.setPixmap(image2_glow)
image3_glow = QPixmap('./images/up_full_glow.png')
image3_glow = image3_glow .scaledToWidth(120)
image3_glow = image3_glow .scaledToHeight(120)
img3_glow = QLabel()
img3_glow.setPixmap(image3_glow)
image4_glow = QPixmap('./images/up_open_glow.png')
image4_glow = image4_glow .scaledToWidth(120)
image4_glow = image4_glow .scaledToHeight(120)
img4_glow = QLabel()
img4_glow.setPixmap(image4_glow)


#images_glow = [img0_glow, img1_glow, img2_glow, img3_glow, img4_glow]

grid.addWidget(btn0, 0, 0)
grid.addWidget(btn1, 0, 1)
grid.addWidget(btn2, 0, 2)
grid.addWidget(btn3, 0, 3)
grid.addWidget(btn4, 0, 4)
grid.addWidget(btn5, 0, 5)
grid.addWidget(btn6, 0, 6)
grid.addWidget(btn7, 0, 7)


win.show()

sys.exit(app.exec_())