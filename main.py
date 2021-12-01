import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
from PyQt5.QtCore import (Qt, pyqtSignal, QRect)


class Image_object():    
    def image(column):
        image = QPixmap("./images/dot.png")
        image = image.scaledToWidth(120)
        image = image.scaledToHeight(120)
        img = QLabel()
        img.setPixmap(image)
        grid.addWidget(img, 0, column)

    def mousePressEvent(self, img):
        print ("clicked")


class MyWidget(QWidget):
     def mousePressEvent(self, event):
        print ("clicked")




app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Anitrone")
window.setGeometry(200, 200, 820, 120)
window.setStyleSheet("background: black;")

grid = QGridLayout()

window.setLayout(grid)

Image_object.image(0)
Image_object.image(1)
Image_object.image(2)
Image_object.image(3)
Image_object.image(4)
Image_object.image(5)
Image_object.image(6)
Image_object.image(7)

widget = MyWidget()
widget.show()

window.show()
sys.exit(app.exec_())