import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
class Image_object():
    def image():
        image = QPixmap("./images/dot.png")
        image = QPixmap.scaled(120, 120, QtCore.Qt.KeepAspectRatio)
        img = QLabel()
        img.setPixmap(image)
        grid.addWidget(img, 0, 0)
        




app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Anitrone")
window.setGeometry(200, 200, 820, 120)
window.setStyleSheet("background: black;")

grid = QGridLayout()

window.setLayout(grid)

Image_object.image()

window.show()
sys.exit(app.exec())