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
    isGlowing = False  # Track if the element is glowing

    def __init__(self, elementIndex):
        super(Element, self).__init__()
        self.elementIndex = elementIndex
        self.setPixmap(images[0])

    def mousePressEvent(self, event):
        # If this element is already glowing, do nothing
        if self.isGlowing:
            return
        
        self.imgIndex = (self.imgIndex + 1) % len(images)
        self.setPixmap(images[self.imgIndex])

        # Trigger glow for the first sprite only
        if self.elementIndex == 0:
            self.isGlowing = True
            self.glow()

    def glow(self):
        glow = Fade()
        glow.setPixmap(images_glow[self.imgIndex])
        grid.addWidget(glow, 0, self.elementIndex)

        # Remove glow effect after fading out
        QtCore.QTimer.singleShot(RELEASE, self.removeGlow)

    def removeGlow(self):
        self.isGlowing = False  # Reset glow state


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
        
        # Only connect glow for the first sprite (index 0)
        self.worker.glow0.connect(button0.glow)

        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.worker.finished.connect(self.thread.deleteLater)
        # Start the thread
        self.thread.start()


class Render(QObject):
    finished = pyqtSignal()
    
    glow0 = pyqtSignal()

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

        # Update composite image size to accommodate only the first sprite
        composite_img = np.zeros((220, 220, 4), dtype=np.uint8)  # Create a transparent image for the single sprite

        # Render the sprite animation frames
        for i in range(int(duration * FPS)):
            # Clear the composite image for each frame
            composite_img.fill(0)

            # Calculate the current frame's glow intensity factor
            glow_factor = 0
            if i < FPS:  # First second for glowing
                glow_factor = i / FPS  # Fade in
            elif i >= int(duration * FPS) - FPS:  # Last second for glowing
                glow_factor = (int(duration * FPS) - i) / FPS  # Fade out

            # Only render the first sprite
            j = 0  # Only the first sprite (index 0)

            # Get the current sprite and its glow image
            sprite_img = images[j]
            glow_img = images_glow[j]

            # Convert QPixmap to NumPy array
            qimage_sprite = sprite_img.toImage()
            qimage_glow = glow_img.toImage()

            width, height = qimage_sprite.width(), qimage_sprite.height()
            ptr_sprite = qimage_sprite.bits()
            ptr_sprite.setsize(qimage_sprite.byteCount())
            img_data_sprite = np.array(ptr_sprite).reshape(height, width, 4)  # Convert to RGBA

            ptr_glow = qimage_glow.bits()
            ptr_glow.setsize(qimage_glow.byteCount())
            img_data_glow = np.array(ptr_glow).reshape(height, width, 4)  # Convert to RGBA

            # Blend the current sprite and glow image based on the glow factor
            blended_image = cv2.addWeighted(img_data_sprite, 1 - glow_factor, img_data_glow, glow_factor, 0)

            # Overlay the blended image onto the composite image
            composite_img[:, :] = blended_image  # Place the blended sprite in the composite

            # Save the composite frame
            file_name = os.path.join(output_dir, f'frame_{i:04d}.png')
            cv2.imwrite(file_name, composite_img)

        # Once all frames are saved, call FFmpeg to convert to transparent video
        self.convert_to_video(output_dir, FPS)

        self.finished.emit()


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
