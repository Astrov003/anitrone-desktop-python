import os
from moviepy.editor import VideoFileClip, ImageClip, clips_array
from PIL import Image

def create_video_canvas(tempo):
    if tempo == 120:
        duration = 8
        frames = 30
    elif tempo == 150:
        duration = 6.4
        frames = 24
    elif tempo == 180:
        duration = 5.35
        frames = 20

    # Define the folder containing your APNG files and the output video name
    apng_folder = ''  # Adjust this to your APNG folder path if needed
    output_video = 'output_video.mp4'
    target_width = 1760
    target_height = 220

    # Step 1: Extract the first frames from APNG
    first_frame_clips = []
    for i in range(8):
        input_apng = os.path.join(apng_folder, f'video_{i}.png')
        
        # Open the APNG and get the first frame
        with Image.open(input_apng) as img:
            img.seek(0)  # Get the first frame
            first_frame = img.copy()  # Copy the first frame for processing
        
        # Create an ImageClip from the first frame
        first_frame_clip = ImageClip(first_frame).set_duration(duration)  # Set duration for specified time
        
        # Resize the frame to the target height and maintain aspect ratio
        aspect_ratio = first_frame.width / first_frame.height
        new_width = int(target_height * aspect_ratio)
        
        # Resize the frame clip
        first_frame_clip = first_frame_clip.resize(newsize=(new_width, target_height))
        
        first_frame_clips.append(first_frame_clip)

    # Step 2: Concatenate frames horizontally
    # Create a horizontal stack of clips
    final_clip = clips_array([[clip for clip in first_frame_clips]])

    # Step 3: Write the final video
    final_clip.write_videofile(output_video, fps=30)

    print("Canvas created")

