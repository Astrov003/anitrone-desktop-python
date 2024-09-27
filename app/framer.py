from .render import render_frames

def frame_animation(tempo, img_indices):
    FPS = 30

    if tempo == 120:
        duration = 8
    elif tempo == 150:
        duration = 6.4
    elif tempo == 180:
        duration = 5.35

    for i in range(int(duration * FPS)):
        if duration == 8:
            if i == 0:
                render_frames(img_indices[0], i)
            elif i == 30:
                render_frames(img_indices[1], i)
            elif i == 60:
                render_frames(img_indices[2], i)
            elif i == 90:
                render_frames(img_indices[3], i)
            elif i == 120:
                render_frames(img_indices[4], i)
            elif i == 150:
                render_frames(img_indices[5], i)
            elif i == 180:
                render_frames(img_indices[6], i)
            elif i == 210:
                render_frames(img_indices[7], i)
        elif duration == 6.4:
            if i == 0:
                self.glow0.emit()
            elif i == 24:
                self.glow1.emit()
            elif i == 48:
                self.glow2.emit()
            elif i == 72:
                self.glow3.emit()
            elif i == 96:
                self.glow4.emit()
            elif i == 120:
                self.glow5.emit()
            elif i == 144:
                self.glow6.emit()
            elif i == 168:
                self.glow7.emit()
        elif duration == 5.35:
            if i == 0:
                self.glow0.emit()
            elif i == 20:
                self.glow1.emit()
            elif i == 40:
                self.glow2.emit()
            elif i == 60:
                self.glow3.emit()
            elif i == 80:
                self.glow4.emit()
            elif i == 100:
                self.glow5.emit()
            elif i == 120:
                self.glow6.emit()
            elif i == 140:
                self.glow7.emit()