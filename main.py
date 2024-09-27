from PyQt5.QtWidgets import QLabel, QApplication, QGridLayout, QWidget, QVBoxLayout, QHBoxLayout, QRadioButton, QPushButton, QGroupBox, QProgressBar
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, pyqtSignal, QThread, pyqtSlot
import sys
import os

# Render imports
from framer import frame_animation
from create_videos import create_group_videos
from create_canvas import create_image_canvas
from concat_videos import concat_final_videos
from cleanup import clean_up_files
import time  # For simulating the process time

# fix menu path when compiling to one file
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

app = QApplication(sys.argv)

# Load sprite images
images = [
    QPixmap(resource_path(f'images/sprite_{i}.png')).scaled(110, 110, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
    for i in range(6)
]

class Element(QLabel):
    # Signal to notify the window whenever the imgIndex changes
    indexChanged = pyqtSignal(int, int)

    def __init__(self, elementIndex):
        super(Element, self).__init__()
        self.elementIndex = elementIndex
        self.imgIndex = 0  # Instance variable to track the image index
        self.setPixmap(images[0])
        self.updatePixmap()

    def mousePressEvent(self, event):
        # Update the imgIndex on click
        self.imgIndex = (self.imgIndex + 1) % len(images)
        self.updatePixmap()

        # Emit signal that the imgIndex has changed
        self.indexChanged.emit(self.elementIndex, self.imgIndex)

    def updatePixmap(self):
        # Update the pixmap of the QLabel based on imgIndex
        self.setPixmap(images[self.imgIndex])

class RenderThread(QThread):
    progressChanged = pyqtSignal(int)

    def __init__(self, tempo, elementStates):
        super(RenderThread, self).__init__()
        self.tempo = tempo
        self.elementStates = elementStates

    def run(self):
        # Simulate each step of rendering with time delay and emit progress
        steps = [20, 40, 60, 80, 100]
        frame_animation(self.tempo, self.elementStates)  # Simulate task
        self.progressChanged.emit(steps[0])
        time.sleep(1)  # Simulate time-consuming task

        create_group_videos(self.tempo)  # Simulate task
        self.progressChanged.emit(steps[1])
        time.sleep(1)

        create_image_canvas(self.tempo)  # Simulate task
        self.progressChanged.emit(steps[2])
        time.sleep(1)

        # concat_final_videos(self.tempo)  # Simulate task
        # self.progressChanged.emit(steps[3])
        # time.sleep(1)

        # clean_up_files()  # Simulate task
        # self.progressChanged.emit(steps[4])
        # time.sleep(1)

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle('Anitrone 2.0')
        self.setGeometry(480, 480, 960, 110)  # Set the window size to 960x110
        self.setStyleSheet("background: black;")

        # Main layout
        mainLayout = QHBoxLayout(self)

        # Grid layout for elements
        grid = QGridLayout()
        self.elements = [Element(i) for i in range(8)]
        self.elementStates = [0] * len(self.elements)  # Track imgIndex of each element

        # Connect each element's indexChanged signal to the state handler
        for i, element in enumerate(self.elements):
            element.indexChanged.connect(self.updateElementState)
            grid.addWidget(element, 0, i)

        # Add the grid layout to the main layout
        mainLayout.addLayout(grid)

        # Vertical layout for radio buttons and the start button
        controlLayout = QVBoxLayout()

        # Group box to hold radio buttons and labels
        radioGroup = QGroupBox("Select Tempo")
        radioLayout = QVBoxLayout()

        # Radio buttons and labels
        self.tempo120 = QRadioButton("120 BPM")
        self.tempo150 = QRadioButton("150 BPM")
        self.tempo180 = QRadioButton("180 BPM")
        self.tempo120.setChecked(True)  # Set default to 120

        # Apply stylesheet for white text
        radioStylesheet = """
            QRadioButton {
                color: white;
            }
        """
        self.tempo120.setStyleSheet(radioStylesheet)
        self.tempo150.setStyleSheet(radioStylesheet)
        self.tempo180.setStyleSheet(radioStylesheet)

        # Add radio buttons to the radio layout
        radioLayout.addWidget(self.tempo120)
        radioLayout.addWidget(self.tempo150)
        radioLayout.addWidget(self.tempo180)

        # Set the layout to the group box
        radioGroup.setLayout(radioLayout)

        # Add radio group to control layout
        controlLayout.addWidget(radioGroup)

        # Render button (start button)
        self.startButton = QPushButton("Render")
        self.startButton.setStyleSheet("""
            QPushButton {
                border: 2px solid white;
                padding: 10px;
                color: white;
                background-color: black;
            }
            QPushButton:hover {
                background-color: gray;
            }
        """)
        self.startButton.clicked.connect(self.start)

        # Add the start button to the control layout
        controlLayout.addWidget(self.startButton)

        # Progress bar
        self.progressBar = QProgressBar()
        self.progressBar.setStyleSheet("""
            QProgressBar {
                color: white;
                text-align: center;
            }
            QProgressBar::chunk {
                background-color: #00ff00;
            }
        """)
        self.progressBar.setValue(0)  # Set initial value
        controlLayout.addWidget(self.progressBar)

        # Add the control layout to the main layout
        mainLayout.addLayout(controlLayout)

    def updateElementState(self, elementIndex, imgIndex):
        # Update the internal state of elements whenever an imgIndex changes
        self.elementStates[elementIndex] = imgIndex

    def start(self):
        # Check which radio button is selected and get the corresponding tempo
        if self.tempo120.isChecked():
            tempo = 120
        elif self.tempo150.isChecked():
            tempo = 150
        else:
            tempo = 180

        # Start the rendering process in a separate thread
        self.renderThread = RenderThread(tempo, self.elementStates)
        self.renderThread.progressChanged.connect(self.updateProgress)
        self.renderThread.start()

    @pyqtSlot(int)
    def updateProgress(self, value):
        # Update the progress bar based on the emitted signal
        self.progressBar.setValue(value)

# main
win = MyWindow()
win.show()
sys.exit(app.exec_())
