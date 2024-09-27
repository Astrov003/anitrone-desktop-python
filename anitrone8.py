from PyQt5.QtWidgets import QLabel, QApplication, QGridLayout, QWidget, QGraphicsOpacityEffect, QShortcut
from PyQt5.QtGui import QPixmap, QKeySequence
from PyQt5.QtCore import Qt, QObject, QThread, pyqtSignal
from PyQt5 import QtCore
import sys
import os

# Import necessary libraries for image rendering
import cv2
import numpy as np
import datetime
import subprocess
import shutil

# Constants for animation
ATTACK = 200
HOLD = ATTACK + 0
RELEASE = 1700
FADE_RANGE = 1

# Fix menu path when compiling to one file
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

app = QApplication(sys.argv)
grid = QGridLayout()

# Load sprite images
images = [
    QPixmap(resource_path(f'images/sprite_{i}.png')).scaled(220, 220, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
    for i in range(6)
]

# Glow images
images_glow = [
    QPixmap(resource_path(f'images/sprite_{i}_glow.png')).scaled(220, 220, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
    for i in range(6)
]

class Element(QLabel):
    imgIndex = 0
    elementIndex = 0

    def __init__(self, elementIndex):
        super(Element, self).__init__()
        self.elementIndex = elementIndex
        self.setPixmap(images[0])

    def mousePressEvent(self, event):
        self.imgIndex = (self.imgIndex + 1) % len(images)
        self.setPixmap(images[self.imgIndex])

    def glow(self):
        glow = Fade()
        glow.setPixmap(images_glow[self.imgIndex])
        grid.addWidget(glow, 0, self.elementIndex)


class Fade(QLabel):
    def __init__(self):
        super().__init__()
        self.fadeIn()
        QtCore.QTimer.singleShot(HOLD, lambda: self.fadeOut())

    def fadeIn(self):   
        self.effect = QGraphicsOpacityEffect()
        self.setGraphicsEffect(self.effect)
        self.animation = QtCore.QPropertyAnimation(self.effect, b"opacity")
        self.animation.setDuration(ATTACK)
        self.animation.setStartValue(0)
        self.animation.setEndValue(FADE_RANGE)
        self.animation.start()

    def fadeOut(self):
        self.effect = QGraphicsOpacityEffect()
        self.setGraphicsEffect(self.effect)
        self.animation = QtCore.QPropertyAnimation(self.effect, b"opacity")
        self.animation.setDuration(RELEASE)
        self.animation.setStartValue(FADE_RANGE)
        self.animation.setEndValue(0)
        self.animation.start()


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle('Anitrone')
        self.setGeometry(0, 200, 1920, 220)
        self.setStyleSheet("background: black;")
        self.setLayout(grid)
        
        # Create buttons here
        self.create_buttons()

        self.keyStroke()

    def create_buttons(self):
        global button0, button1, button2, button3, button4, button5, button6, button7
        
        button0 = Element(0)
        button1 = Element(1)
        button2 = Element(2)
        button3 = Element(3)
        button4 = Element(4)
        button5 = Element(5)
        button6 = Element(6)
        button7 = Element(7)

        grid.addWidget(button0, 0, 0)
        grid.addWidget(button1, 0, 1)
        grid.addWidget(button2, 0, 2)
        grid.addWidget(button3, 0, 3)
        grid.addWidget(button4, 0, 4)
        grid.addWidget(button5, 0, 5)
        grid.addWidget(button6, 0, 6)
        grid.addWidget(button7, 0, 7)

    def keyStroke(self):
        self.tempo120 = QShortcut(QKeySequence('Ctrl+1'), self)
        self.tempo120.activated.connect(lambda *_: self.start(120))
        self.tempo150 = QShortcut(QKeySequence('Ctrl+2'), self)
        self.tempo150.activated.connect(lambda *_: self.start(150))
        self.tempo180 = QShortcut(QKeySequence('Ctrl+3'), self)
        self.tempo180.activated.connect(lambda *_: self.start(180))

    tempo = 0
    def start(self, tempo):
        MyWindow.tempo = tempo

        # Create a QThread object
        self.thread = QThread()
        # Create a worker object
        self.worker = Render()
        # Move worker to the thread
        self.worker.moveToThread(self.thread)

        # Connect signals and slots
        self.thread.started.connect(self.worker.render)
        
        self.worker.glow0.connect(button0.glow)
        self.worker.glow1.connect(button1.glow)
        self.worker.glow2.connect(button2.glow)
        self.worker.glow3.connect(button3.glow)
        self.worker.glow4.connect(button4.glow)
        self.worker.glow5.connect(button5.glow)
        self.worker.glow6.connect(button6.glow)
        self.worker.glow7.connect(button7.glow)

        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.worker.finished.connect(self.thread.deleteLater)
        # Start the thread
        self.thread.start()


class Render(QObject):
    finished = pyqtSignal()
    
    glow0 = pyqtSignal()
    glow1 = pyqtSignal()
    glow2 = pyqtSignal()
    glow3 = pyqtSignal()
    glow4 = pyqtSignal()
    glow5 = pyqtSignal()
    glow6 = pyqtSignal()
    glow7 = pyqtSignal()

    def __init__(self):
        super().__init__()

    def render(self):
        FPS = 30
        time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        
        # Directory to save PNG files (temporary directory)
        output_dir = f'./output_{time_stamp}/'
        os.makedirs(output_dir, exist_ok=True)

        # Determine the duration based on tempo
        if MyWindow.tempo == 120:
            duration = 8
        elif MyWindow.tempo == 150:
            duration = 6.4
        elif MyWindow.tempo == 180:
            duration = 5.35

        # Update composite image size to accommodate 8 sprites
        composite_img = np.zeros((220, 8 * 220, 4), dtype=np.uint8)  # Create a transparent image for the composite

        # Render the sprite animation frames
        for i in range(int(duration * FPS)):
            # Clear the composite image for each frame
            composite_img.fill(0)

            # Calculate current sprite index based on frame
            for j in range(8):  # Iterate through all sprites
                sprite_index = (i // (FPS // len(images))) % len(images)
                sprite_img = images[sprite_index]

                # Convert QPixmap to NumPy array
                qimage = sprite_img.toImage()
                width, height = qimage.width(), qimage.height()
                ptr = qimage.bits()
                ptr.setsize(qimage.byteCount())
                img_data = np.array(ptr).reshape(height, width, 4)  # Convert to RGBA

                # Overlay the sprite onto the composite image at the correct position
                x_offset = j * 220  # Calculate the horizontal position for the sprite
                composite_img[:, x_offset:x_offset + 220, :] = img_data  # Place the sprite in the composite

                # Emit glow signals based on frame number
                if self.should_glow(i, duration, j):
                    getattr(self, f'glow{j}').emit()  # Emit the corresponding glow signal

            # Save the composite frame
            file_name = os.path.join(output_dir, f'frame_{i:04d}.png')
            cv2.imwrite(file_name, composite_img)

        # Once all frames are saved, call FFmpeg to convert to transparent video
        self.convert_to_video(output_dir, FPS)

        self.finished.emit()

    def should_glow(self, frame_index, duration, sprite_index):
        # Logic to determine if the sprite should glow in this frame based on the duration
        if duration == 8:
            return frame_index in [0, 30, 60, 90, 120, 150, 180, 210] and sprite_index == frame_index // 30
        elif duration == 6.4:
            return frame_index in [0, 24, 48, 72, 96, 120, 144, 168] and sprite_index == frame_index // 24
        elif duration == 5.35:
            return frame_index in [0, 20, 40, 60, 80, 100, 120, 140] and sprite_index == frame_index // 20
        return False

    def convert_to_video(self, output_dir, fps):
        # Path to the final video file saved in the script directory
        video_file = os.path.join('.', 'output_video.webm')

        # FFmpeg command to convert PNG sequence to WebM video with transparency
        ffmpeg_command = [
            'ffmpeg', '-framerate', str(fps),
            '-i', os.path.join(output_dir, 'frame_%04d.png'),
            '-vf', 'scale=out_color_matrix=bt709',  # Ensure correct color handling
            '-c:v', 'libvpx-vp9', '-pix_fmt', 'yuva420p',  # VP9 codec with alpha channel
            video_file
        ]

        try:
            # Run the FFmpeg command
            subprocess.run(ffmpeg_command, check=True)
            print(f"Video file created: {video_file}")
        except subprocess.CalledProcessError as e:
            print(f"FFmpeg error: {e}")

        # Optionally: clean up PNG frames after video creation
        shutil.rmtree(output_dir)
        print("PNG frames cleaned up.")



# Main execution
win = MyWindow()

# Create button elements
buttons = [Element(i) for i in range(8)]
for i, button in enumerate(buttons):
    grid.addWidget(button, 0, i)

win.show()
sys.exit(app.exec_())
