from render_frames import render_image_frames

def frame_animation(tempo, img_indices):
    FPS = 30

    if tempo == 120:
        duration = 8
        frames = 30
    elif tempo == 150:
        duration = 6.4
        frames = 24
    elif tempo == 180:
        duration = 5.35
        frames = 20

    for i in range(int(duration * FPS)):
        if duration == 8:
            if i == 0:
                render_image_frames(img_indices[0], i, frames)
            elif i == 30:
                render_image_frames(img_indices[1], i, frames)
            elif i == 60:
                render_image_frames(img_indices[2], i, frames)
            elif i == 90:
                render_image_frames(img_indices[3], i, frames)
            elif i == 120:
                render_image_frames(img_indices[4], i, frames)
            elif i == 150:
                render_image_frames(img_indices[5], i, frames)
            elif i == 180:
                render_image_frames(img_indices[6], i, frames)
            elif i == 210:
                render_image_frames(img_indices[7], i, frames)
        elif duration == 6.4:
            if i == 0:
                render_image_frames(img_indices[0], i, frames)
            elif i == 24:
                render_image_frames(img_indices[1], i, frames)
            elif i == 48:
                render_image_frames(img_indices[2], i, frames)
            elif i == 72:
                render_image_frames(img_indices[3], i, frames)
            elif i == 96:
                render_image_frames(img_indices[4], i, frames)
            elif i == 120:
                render_image_frames(img_indices[5], i, frames)
            elif i == 144:
                render_image_frames(img_indices[6], i, frames)
            elif i == 168:
                render_image_frames(img_indices[7], i, frames)
        elif duration == 5.35:
            if i == 0:
                render_image_frames(img_indices[0], i, frames)
            elif i == 20:
                render_image_frames(img_indices[1], i, frames)
            elif i == 40:
                render_image_frames(img_indices[2], i, frames)
            elif i == 60:
                render_image_frames(img_indices[3], i, frames)
            elif i == 80:
                render_image_frames(img_indices[4], i, frames)
            elif i == 100:
                render_image_frames(img_indices[5], i, frames)
            elif i == 120:
                render_image_frames(img_indices[6], i, frames)
            elif i == 140:
                render_image_frames(img_indices[7], i, frames)