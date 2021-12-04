import sys
from PyQt5.QtWidgets import QApplication, QGridLayout, QWidget, QLabel, QGraphicsOpacityEffect, QShortcut
from PyQt5.QtGui import QPixmap, QKeySequence
from PyQt5 import QtCore
from PyQt5.QtCore import Qt


ATTACK = 100
HOLD = 0
RELEASE = 100


#=== ANIMATION PLAY ======

def play(TEMPO):
    if TEMPO == 120:
        switch_interval = 1000
    if TEMPO == 150:
        switch_interval = 800
    if TEMPO == 180:
        switch_interval = 666
    trigger_glow0()
    QtCore.QTimer.singleShot(switch_interval, lambda: trigger_glow1())
    QtCore.QTimer.singleShot(switch_interval*2, lambda: trigger_glow2())
    QtCore.QTimer.singleShot(switch_interval*3, lambda: trigger_glow3())
    QtCore.QTimer.singleShot(switch_interval*4, lambda: trigger_glow4())
    QtCore.QTimer.singleShot(switch_interval*5, lambda: trigger_glow5())
    QtCore.QTimer.singleShot(switch_interval*6, lambda: trigger_glow6())
    QtCore.QTimer.singleShot(switch_interval*7, lambda: trigger_glow7())


#=== TRIGGER GLOW SEPARATE FOR ALL 8 BTNs =====

def trigger_glow0():
    global btn0_image_counter
    for i in range(5):
        if btn0_image_counter == i:     
            btn0_glow = FadeInImage0()
            btn0_glow.setPixmap(arr_images_glow[i])
            grid.addWidget(btn0_glow, 0, 0)

def trigger_glow1():
    global btn1_image_counter
    for i in range(5):
        if btn1_image_counter == i:     
            btn1_glow = FadeInImage0()
            btn1_glow.setPixmap(arr_images_glow[i])
            grid.addWidget(btn1_glow, 0, 1)

def trigger_glow2():
    global btn2_image_counter
    for i in range(5):
        if btn2_image_counter == i:     
            btn2_glow = FadeInImage0()
            btn2_glow.setPixmap(arr_images_glow[i])
            grid.addWidget(btn2_glow, 0, 2)

def trigger_glow3():
    global btn3_image_counter
    for i in range(5):
        if btn3_image_counter == i:     
            btn3_glow = FadeInImage0()
            btn3_glow.setPixmap(arr_images_glow[i])
            grid.addWidget(btn3_glow, 0, 3)

def trigger_glow4():
    global btn4_image_counter
    for i in range(5):
        if btn4_image_counter == i:     
            btn4_glow = FadeInImage0()
            btn4_glow.setPixmap(arr_images_glow[i])
            grid.addWidget(btn4_glow, 0, 4)

def trigger_glow5():
    global btn5_image_counter
    for i in range(5):
        if btn5_image_counter == i:     
            btn5_glow = FadeInImage0()
            btn5_glow.setPixmap(arr_images_glow[i])
            grid.addWidget(btn5_glow, 0, 5)

def trigger_glow6():
    global btn6_image_counter
    for i in range(5):
        if btn6_image_counter == i:     
            btn6_glow = FadeInImage0()
            btn6_glow.setPixmap(arr_images_glow[i])
            grid.addWidget(btn6_glow, 0, 6)

def trigger_glow7():
    global btn7_image_counter
    for i in range(5):
        if btn7_image_counter == i:     
            btn7_glow = FadeInImage0()
            btn7_glow.setPixmap(arr_images_glow[i])
            grid.addWidget(btn7_glow, 0, 7)


#====== FADE IN LOGIC =====================

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


#====== IMAGE CLASS + IMAGE CLICK EVENT ======

class Image0(QLabel):
    def mousePressEvent(self, event):
        global btn0_image_counter
        if btn0_image_counter == 0:
            btn0.setPixmap(arr_images_base[1])
            btn0_image_counter = 1
        elif btn0_image_counter == 1:
            btn0.setPixmap(arr_images_base[2])
            btn0_image_counter = 2
        elif btn0_image_counter == 2:
            btn0.setPixmap(arr_images_base[3])
            btn0_image_counter = 3
        elif btn0_image_counter == 3:
            btn0.setPixmap(arr_images_base[4])
            btn0_image_counter = 4
        elif btn0_image_counter == 4:
            btn0.setPixmap(arr_images_base[0])
            btn0_image_counter = 0
        
class Image1(QLabel):     
    def mousePressEvent(self, event):
        global btn1_image_counter
        if btn1_image_counter == 0:
            btn1.setPixmap(arr_images_base[1])
            btn1_image_counter = 1
        elif btn1_image_counter == 1:
            btn1.setPixmap(arr_images_base[2])
            btn1_image_counter = 2
        elif btn1_image_counter == 2:
            btn1.setPixmap(arr_images_base[3])
            btn1_image_counter = 3
        elif btn1_image_counter == 3:
            btn1.setPixmap(arr_images_base[4])
            btn1_image_counter = 4
        elif btn1_image_counter == 4:
            btn1.setPixmap(arr_images_base[0])
            btn1_image_counter = 0

class Image2(QLabel):     
    def mousePressEvent(self, event):
        global btn2_image_counter
        if btn2_image_counter == 0:
            btn2.setPixmap(arr_images_base[1])
            btn2_image_counter = 1
        elif btn2_image_counter == 1:
            btn2.setPixmap(arr_images_base[2])
            btn2_image_counter = 2
        elif btn2_image_counter == 2:
            btn2.setPixmap(arr_images_base[3])
            btn2_image_counter = 3
        elif btn2_image_counter == 3:
            btn2.setPixmap(arr_images_base[4])
            btn2_image_counter = 4
        elif btn2_image_counter == 4:
            btn2.setPixmap(arr_images_base[0])
            btn2_image_counter = 0

class Image3(QLabel):     
    def mousePressEvent(self, event):
        global btn3_image_counter
        if btn3_image_counter == 0:
            btn3.setPixmap(arr_images_base[1])
            btn3_image_counter = 1
        elif btn3_image_counter == 1:
            btn3.setPixmap(arr_images_base[2])
            btn3_image_counter = 2
        elif btn3_image_counter == 2:
            btn3.setPixmap(arr_images_base[3])
            btn3_image_counter = 3
        elif btn3_image_counter == 3:
            btn3.setPixmap(arr_images_base[4])
            btn3_image_counter = 4
        elif btn3_image_counter == 4:
            btn3.setPixmap(arr_images_base[0])
            btn3_image_counter = 0

class Image4(QLabel):     
    def mousePressEvent(self, event):
        global btn4_image_counter
        if btn4_image_counter == 0:
            btn4.setPixmap(arr_images_base[1])
            btn4_image_counter = 1
        elif btn4_image_counter == 1:
            btn4.setPixmap(arr_images_base[2])
            btn4_image_counter = 2
        elif btn4_image_counter == 2:
            btn4.setPixmap(arr_images_base[3])
            btn4_image_counter = 3
        elif btn4_image_counter == 3:
            btn4.setPixmap(arr_images_base[4])
            btn4_image_counter = 4
        elif btn4_image_counter == 4:
            btn4.setPixmap(arr_images_base[0])
            btn4_image_counter = 0

class Image5(QLabel):     
    def mousePressEvent(self, event):
        global btn5_image_counter
        if btn5_image_counter == 0:
            btn5.setPixmap(arr_images_base[1])
            btn5_image_counter = 1
        elif btn5_image_counter == 1:
            btn5.setPixmap(arr_images_base[2])
            btn5_image_counter = 2
        elif btn5_image_counter == 2:
            btn5.setPixmap(arr_images_base[3])
            btn5_image_counter = 3
        elif btn5_image_counter == 3:
            btn5.setPixmap(arr_images_base[4])
            btn5_image_counter = 4
        elif btn5_image_counter == 4:
            btn5.setPixmap(arr_images_base[0])
            btn5_image_counter = 0

class Image6(QLabel):     
    def mousePressEvent(self, event):
        global btn6_image_counter
        if btn6_image_counter == 0:
            btn6.setPixmap(arr_images_base[1])
            btn6_image_counter = 1
        elif btn6_image_counter == 1:
            btn6.setPixmap(arr_images_base[2])
            btn6_image_counter = 2
        elif btn6_image_counter == 2:
            btn6.setPixmap(arr_images_base[3])
            btn6_image_counter = 3
        elif btn6_image_counter == 3:
            btn6.setPixmap(arr_images_base[4])
            btn6_image_counter = 4
        elif btn6_image_counter == 4:
            btn6.setPixmap(arr_images_base[0])
            btn6_image_counter = 0

class Image7(QLabel):     
    def mousePressEvent(self, event):
        global btn7_image_counter
        if btn7_image_counter == 0:
            btn7.setPixmap(arr_images_base[1])
            btn7_image_counter = 1
        elif btn7_image_counter == 1:
            btn7.setPixmap(arr_images_base[2])
            btn7_image_counter = 2
        elif btn7_image_counter == 2:
            btn7.setPixmap(arr_images_base[3])
            btn7_image_counter = 3
        elif btn7_image_counter == 3:
            btn7.setPixmap(arr_images_base[4])
            btn7_image_counter = 4
        elif btn7_image_counter == 4:
            btn7.setPixmap(arr_images_base[0])
            btn7_image_counter = 0


    
#====== MAIN WINDOW CLASS =================
class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle('Anitrone')
        self.setGeometry(200, 200, 820, 120)
        self.setStyleSheet("background: black;")
        self.setLayout(grid)
        self.initUI()

    # === Keyboard Shortcut Event ======
    def initUI(self):
        self.tempo120 = QShortcut(QKeySequence('Ctrl+1'), self)
        self.tempo120.activated.connect(lambda *_: play(120))
        self.tempo150 = QShortcut(QKeySequence('Ctrl+2'), self)
        self.tempo150.activated.connect(lambda *_: play(150))
        self.tempo180 = QShortcut(QKeySequence('Ctrl+3'), self)
        self.tempo180.activated.connect(lambda *_: play(180))


#==== MAIN ================

app = QApplication(sys.argv)
grid = QGridLayout()

win = MyWindow()

###====== IMAGE VARIABLES ================================================
btn0_image_counter = 0
btn1_image_counter = 0
btn2_image_counter = 0
btn3_image_counter = 0
btn4_image_counter = 0
btn5_image_counter = 0
btn6_image_counter = 0
btn7_image_counter = 0

image0 = QPixmap('./images/dot.png')
image0 = image0.scaledToWidth(120, Qt.SmoothTransformation)
image0 = image0.scaledToHeight(120, Qt.SmoothTransformation)
image1 = QPixmap('./images/down_full.png')
image1 = image1.scaledToWidth(120, Qt.SmoothTransformation)
image1 = image1.scaledToHeight(120, Qt.SmoothTransformation)
image2 = QPixmap('./images/down_open.png')
image2 = image2.scaledToWidth(120, Qt.SmoothTransformation)
image2 = image2.scaledToHeight(120, Qt.SmoothTransformation)
image3 = QPixmap('./images/up_full.png')
image3 = image3.scaledToWidth(120, Qt.SmoothTransformation)
image3 = image3.scaledToHeight(120, Qt.SmoothTransformation)
image4 = QPixmap('./images/up_open.png')
image4 = image4.scaledToWidth(120, Qt.SmoothTransformation)
image4 = image4.scaledToHeight(120, Qt.SmoothTransformation)

image0_glow = QPixmap('./images/dot_glow.png')
image0_glow = image0_glow.scaledToWidth(120, Qt.SmoothTransformation)
image0_glow = image0_glow.scaledToHeight(120, Qt.SmoothTransformation)
image1_glow = QPixmap('./images/down_full_glow.png')
image1_glow = image1_glow .scaledToWidth(120, Qt.SmoothTransformation)
image1_glow = image1_glow .scaledToHeight(120, Qt.SmoothTransformation)
image2_glow = QPixmap('./images/down_open_glow.png')
image2_glow = image2_glow .scaledToWidth(120, Qt.SmoothTransformation)
image2_glow = image2_glow .scaledToHeight(120, Qt.SmoothTransformation)
image3_glow = QPixmap('./images/up_full_glow.png')
image3_glow = image3_glow .scaledToWidth(120, Qt.SmoothTransformation)
image3_glow = image3_glow .scaledToHeight(120, Qt.SmoothTransformation)
image4_glow = QPixmap('./images/up_open_glow.png')
image4_glow = image4_glow .scaledToWidth(120, Qt.SmoothTransformation)
image4_glow = image4_glow .scaledToHeight(120, Qt.SmoothTransformation)

arr_images_base = [image0, image1, image2, image3, image4]
arr_images_glow = [image0_glow, image1_glow, image2_glow, image3_glow, image4_glow]
#======================================================================


#=== INIATIALIZE IMAGES =====
btn0 = Image0()
btn0.setPixmap(arr_images_base[0])
btn1 = Image1()
btn1.setPixmap(arr_images_base[0])
btn2 = Image2()
btn2.setPixmap(arr_images_base[0])
btn3 = Image3()
btn3.setPixmap(arr_images_base[0])
btn4 = Image4()
btn4.setPixmap(arr_images_base[0])
btn5 = Image5()
btn5.setPixmap(arr_images_base[0])
btn6 = Image6()
btn6.setPixmap(arr_images_base[0])
btn7 = Image7()
btn7.setPixmap(arr_images_base[0])

grid.addWidget(btn0, 0, 0)
grid.addWidget(btn1, 0, 1)
grid.addWidget(btn2, 0, 2)
grid.addWidget(btn3, 0, 3)
grid.addWidget(btn4, 0, 4)
grid.addWidget(btn5, 0, 5)
grid.addWidget(btn6, 0, 6)
grid.addWidget(btn7, 0, 7)



#=== SYSTEM COMMANDS =====
win.show()

sys.exit(app.exec_())