import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore


class Image_object():
    def image(column):
        image = QPixmap("./images/dot.png")
        image = image.scaledToWidth(120)
        image = image.scaledToHeight(120)
        img = QLabel()
        img.setPixmap(image)
        grid.addWidget(img, 0, column)
        img.mousePressEvent(click())
    
    def click():
        print("mrs u picku materinu")




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

window.show()
sys.exit(app.exec())