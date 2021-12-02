import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QLabel, QGraphicsOpacityEffect
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, pyqtSignal, QRect

def fade(widget):
    effect = QGraphicsOpacityEffect()
    widget.setGraphicsEffect(effect)

    animation = QtCore.QPropertyAnimation(effect, b"opacity")
    animation.setDuration(1000)
    animation.setStartValue(0)
    animation.setEndValue(1)
    animation.start()

def unfade(self, widget):
    self.effect = QGraphicsOpacityEffect()
    widget.setGraphicsEffect(self.effect)

    self.animation = QtCore.QPropertyAnimation(self.effect, b"opacity")
    self.animation.setDuration(1000)
    self.animation.setStartValue(0)
    self.animation.setEndValue(1)
    self.animation.start()


class MyWidget(QWidget):

    def image(column):
        grid.addWidget(images[0], 0, column)

    def mousePressEvent(self, event):
        print ("clicked")
        img0.setPixmap(image0_glow)

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

#==== GLOBAL VARIABLES====


#==== MAIN ================

app = QApplication(sys.argv)

#windget = QWidget()
widget = QWidget()
widget.setWindowTitle('Anitrone')
widget.setGeometry(200, 200, 820, 120)
widget.setStyleSheet("background: black;")

# GRID

grid = QGridLayout()
widget.setLayout(grid)


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

image0_glow = QPixmap('./images/dot_glow.png')
image0_glow = image0_glow .scaledToWidth(120)
image0_glow = image0_glow .scaledToHeight(120)
img0_glow = QLabel()
img0_glow.setPixmap(image0_glow)
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


images_glow = [img0_glow, img1_glow, img2_glow, img3_glow, img4_glow]

grid.addWidget(btn0, 0, 0)
grid.addWidget(btn1, 0, 1)
grid.addWidget(btn2, 0, 2)
grid.addWidget(btn3, 0, 3)
grid.addWidget(btn4, 0, 4)
grid.addWidget(btn5, 0, 5)
grid.addWidget(btn6, 0, 6)
grid.addWidget(btn7, 0, 7)

widget.show()

sys.exit(app.exec_())