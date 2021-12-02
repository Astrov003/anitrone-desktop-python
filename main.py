import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
from PyQt5.QtCore import (Qt, pyqtSignal, QRect)


class MyWidget(QWidget):

    def image(column):
        grid.addWidget(images[0], 0, column)

    def mousePressEvent(self, event):
        print ("clicked")
        img0.setPixmap(image0_glow)


app = QApplication(sys.argv)

### BASE IMAGES

image0 = QPixmap('./images/dot.png')
imaeg0 = image0.scaledToWidth(120)
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

grid = QGridLayout()

MyWidget.image(0)
MyWidget.image(1)
MyWidget.image(2)
MyWidget.image(3)
MyWidget.image(4)
MyWidget.image(5)
MyWidget.image(6)
MyWidget.image(7)

#windget = QWidget()
widget = MyWidget()
widget.setWindowTitle('aaa')
widget.setGeometry(200, 200, 820, 120)
widget.setStyleSheet("background: black;")

widget.setLayout(grid)

widget.show()

sys.exit(app.exec_())