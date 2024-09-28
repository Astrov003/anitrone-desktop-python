import sys
import os
import time  # For simulating the process time
from PyQt5.QtWidgets import (
    QLabel, QApplication, QGridLayout, QWidget, QVBoxLayout, QHBoxLayout, 
    QRadioButton, QPushButton, QGroupBox, QProgressBar
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, pyqtSignal, QThread, pyqtSlot

# Render imports
from framer import frame_animation
from create_videos import create_group_videos
from create_canvas import create_image_canvas
from concat_videos import concat_final_videos
from cleanup import clean_up_files

numOfElements = 4

# Helper function for PyInstaller compatibility
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller. """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class Element(QLabel):
    """A QLabel subclass representing an individual sprite element."""
    indexChanged = pyqtSignal(int, int)  # Signal emitted when the image index changes

    def __init__(self, elementIndex, images):
        super().__init__()
        self.elementIndex = elementIndex
        self.imgIndex = 0  # Track the current image index
        self.images = images
        self.setPixmap(self.images[self.imgIndex])
        self.updatePixmap()

    def mousePressEvent(self, event):
        """Handle click event to cycle through sprite images."""
        self.imgIndex = (self.imgIndex + 1) % len(self.images)
        self.updatePixmap()
        self.indexChanged.emit(self.elementIndex, self.imgIndex)  # Emit signal when index changes

    def updatePixmap(self):
        """Update the QLabel's pixmap based on the current imgIndex."""
        self.setPixmap(self.images[self.imgIndex])

class RenderThread(QThread):
    """A QThread subclass to handle the rendering process in the background."""
    progressChanged = pyqtSignal(int)

    def __init__(self, tempo, elementStates):
        super().__init__()
        self.tempo = tempo
        self.elementStates = elementStates

    def run(self):
        """Execute rendering steps with progress signals."""
        steps = [20, 40, 60, 80, 100]

        frame_animation(self.tempo, self.elementStates, numOfElements)
        self.progressChanged.emit(steps[0])

        create_group_videos(self.tempo, numOfElements)
        self.progressChanged.emit(steps[1])

        create_image_canvas(self.tempo, numOfElements)
        self.progressChanged.emit(steps[2])

        concat_final_videos(self.tempo, numOfElements)
        self.progressChanged.emit(steps[3])

        clean_up_files(numOfElements)
        self.progressChanged.emit(steps[4])

class MyWindow(QWidget):
    """Main window that contains the UI for rendering animations."""
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Anitrone 2.0')
        self.setGeometry(480, 480, 550, 110)
        self.setStyleSheet("background: black;")

        self.elementStates = [0] * numOfElements  # Track the state of each element
        self.initUI()

    def initUI(self):
        """Initialize the UI components."""
        mainLayout = QHBoxLayout(self)

        # Load sprite images
        self.images = self.loadImages()

        # Add elements grid
        mainLayout.addLayout(self.createElementsGrid())

        # Add controls (radio buttons, render button, progress bar)
        mainLayout.addLayout(self.createControlPanel())

    def loadImages(self):
        """Load and return a list of QPixmap images."""
        return [
            QPixmap(resource_path(f'images/sprite_{i}.png')).scaled(
                110, 110, Qt.IgnoreAspectRatio, Qt.SmoothTransformation
            ) for i in range(6)
        ]

    def createElementsGrid(self):
        """Create a grid layout for sprite elements."""
        grid = QGridLayout()
        self.elements = [Element(i, self.images) for i in range(numOfElements)]
        
        for i, element in enumerate(self.elements):
            element.indexChanged.connect(self.updateElementState)
            grid.addWidget(element, 0, i)

        return grid

    def createControlPanel(self):
        """Create a control panel layout containing radio buttons and render button."""
        controlLayout = QVBoxLayout()

        # Create tempo radio buttons
        radioGroup = QGroupBox("Select Tempo")
        radioLayout = QVBoxLayout()

        self.tempo120 = self.createRadioButton("120 BPM", True)
        self.tempo150 = self.createRadioButton("150 BPM")
        self.tempo180 = self.createRadioButton("180 BPM")

        radioLayout.addWidget(self.tempo120)
        radioLayout.addWidget(self.tempo150)
        radioLayout.addWidget(self.tempo180)
        radioGroup.setLayout(radioLayout)
        controlLayout.addWidget(radioGroup)

        # Render button
        self.startButton = QPushButton("Render")
        self.startButton.setStyleSheet(self.getButtonStyle())
        self.startButton.clicked.connect(self.start)
        controlLayout.addWidget(self.startButton)

        # Progress bar
        self.progressBar = QProgressBar()
        self.progressBar.setStyleSheet(self.getProgressBarStyle())
        self.progressBar.setValue(0)
        controlLayout.addWidget(self.progressBar)

        return controlLayout

    def createRadioButton(self, text, checked=False):
        """Create a styled QRadioButton."""
        radioButton = QRadioButton(text)
        radioButton.setChecked(checked)
        radioButton.setStyleSheet("""
            QRadioButton { color: white; }
        """)
        return radioButton

    def getButtonStyle(self):
        """Return the style for the render button."""
        return """
            QPushButton {
                border: 2px solid white;
                padding: 10px;
                color: white;
                background-color: black;
            }
            QPushButton:hover {
                background-color: gray;
            }
        """

    def getProgressBarStyle(self):
        """Return the style for the progress bar."""
        return """
            QProgressBar {
                color: black;
                text-align: center;
            }
            QProgressBar::chunk {
                background-color: #01EEDD;
            }
        """

    def updateElementState(self, elementIndex, imgIndex):
        """Update the internal state of the elements when an imgIndex changes."""
        self.elementStates[elementIndex] = imgIndex

    def start(self):
        """Start the rendering process in a separate thread."""
        tempo = self.getSelectedTempo()
        self.renderThread = RenderThread(tempo, self.elementStates)
        self.renderThread.progressChanged.connect(self.updateProgress)
        self.renderThread.start()

    def getSelectedTempo(self):
        """Return the selected tempo based on the radio button selection."""
        if self.tempo120.isChecked():
            return 120
        elif self.tempo150.isChecked():
            return 150
        else:
            return 180

    @pyqtSlot(int)
    def updateProgress(self, value):
        """Update the progress bar based on the emitted progress signal."""
        self.progressBar.setValue(value)

# Main entry point
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Initialize and show main window
    win = MyWindow()
    win.show()

    sys.exit(app.exec_())
