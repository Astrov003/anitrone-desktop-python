import sys
from PyQt5.QtWidgets import QApplication, QGridLayout, QWidget, QLabel, QGraphicsOpacityEffect, QShortcut
from PyQt5.QtGui import QPixmap, QKeySequence
from PyQt5 import QtCore


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
        self.msgSc = QShortcut(QKeySequence('Ctrl+1'), self)
        self.msgSc.activated.connect(lambda *_: trigger_glow())
    

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


def trigger_glow():
    global btn0_image_counter
    if btn0_image_counter == 0:     
        btn0_glow = FadeInImage0()
        btn0_glow.setPixmap(arr_images_glow[0])
        grid.addWidget(btn0_glow, 0, 0)
        
        


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
image0 = image0.scaledToWidth(120)
image0 = image0.scaledToHeight(120)
image1 = QPixmap('./images/down_full.png')
image1 = image1.scaledToWidth(120)
image1 = image1.scaledToHeight(120)
image2 = QPixmap('./images/down_open.png')
image2 = image2.scaledToWidth(120)
image2 = image2.scaledToHeight(120)
image3 = QPixmap('./images/up_full.png')
image3 = image3.scaledToWidth(120)
image3 = image3.scaledToHeight(120)
image4 = QPixmap('./images/up_open.png')
image4 = image4.scaledToWidth(120)
image4 = image4.scaledToHeight(120)

image0_glow = QPixmap('./images/dot_glow.png')
image0_glow = image0_glow.scaledToWidth(120)
image0_glow = image0_glow.scaledToHeight(120)
image1_glow = QPixmap('./images/down_full_glow.png')
image1_glow = image1_glow .scaledToWidth(120)
image1_glow = image1_glow .scaledToHeight(120)
image2_glow = QPixmap('./images/down_open_glow.png')
image2_glow = image2_glow .scaledToWidth(120)
image2_glow = image2_glow .scaledToHeight(120)
image3_glow = QPixmap('./images/up_full_glow.png')
image3_glow = image3_glow .scaledToWidth(120)
image3_glow = image3_glow .scaledToHeight(120)
image4_glow = QPixmap('./images/up_open_glow.png')
image4_glow = image4_glow .scaledToWidth(120)
image4_glow = image4_glow .scaledToHeight(120)

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