from render_frames import render_image_frames

def frame_animation(tempo, img_indices, numOfElements):
    FPS = 30

    if tempo == 120:
        total_frames = 240
        frames_per_element = 60
    elif tempo == 150:
        total_frames = 192
        frames_per_element = 48
    elif tempo == 180:
        total_frames = 160
        frames_per_element = 40

    for i in range(total_frames):
        index = i // frames_per_element       
        if i == (index * frames_per_element):
            render_image_frames(img_indices[index], i, frames_per_element)
