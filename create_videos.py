from PIL import Image
import os

# fix menu path when compiling to one file
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def create_group_videos(tempo, numOfElements):
    # Set the number of frames per group based on the tempo
    if tempo == 120:
        frames = 60
    elif tempo == 150:
        frames = 48
    elif tempo == 180:
        frames = 40
    else:
        raise ValueError("Tempo must be 120, 150, or 180.")

    # Constants
    frame_folder = resource_path("output")
    num_frames_per_group = frames
    num_groups = numOfElements
    duration_per_frame = 1000 // 30  # In milliseconds (for 30 fps)

    for group in range(num_groups):
        frames_for_group = []
        for frame_index in range(num_frames_per_group):
            global_index = group * num_frames_per_group + frame_index
            frame_path = os.path.join(frame_folder, f'frame_{global_index}.png')

            if os.path.exists(frame_path):
                image = Image.open(frame_path)
                frames_for_group.append(image)
            else:
                print(f"Warning: Frame {frame_path} not found.")

        if frames_for_group:
            output_apng_path = f'image_{group}.png'
            frames_for_group[0].save(output_apng_path, save_all=True, append_images=frames_for_group[1:], duration=duration_per_frame, loop=0, format='PNG')
            print(f"APNG for group {group} saved as {output_apng_path}")

    print("APNG creation completed successfully.")

