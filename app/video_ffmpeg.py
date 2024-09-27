import os
import subprocess

# Constants
frame_width = 220
frame_height = 220
num_frames_per_group = 30
num_groups = 8
total_width = frame_width * num_groups  # 1760px
output_video_path = 'output_video.avi'  # Change the output video format to .mov
frame_folder = '../output'  # Change this to your folder path

# Create a temporary file to hold the frame information
frame_list_path = 'frames.txt'

# Prepare the list of frames
with open(frame_list_path, 'w') as f:
    for group in range(num_groups):
        for frame_index in range(num_frames_per_group):
            global_index = group * num_frames_per_group + frame_index
            frame_path = os.path.join(frame_folder, f'frame_{global_index}.png')  # Ensure your frames have an alpha channel
            
            if os.path.exists(frame_path):
                f.write(f"file '{frame_path}'\n")
                f.write(f"duration 0.03333\n")  # Duration for each frame (30 FPS)
            else:
                print(f"Warning: Frame {frame_path} not found.")

# Run ffmpeg to create the video
subprocess.run([
    'ffmpeg',
    '-y',  # Overwrite output files
    '-f', 'concat',  # Use concat demuxer
    '-safe', '0',  # Allow unsafe file paths
    '-i', frame_list_path,  # Input the list of frames
    '-c:v', 'png',  # Use PNG codec for lossless video
    '-pix_fmt', 'yuva420p',  # Set pixel format to include alpha channel
    output_video_path
])

# Clean up the temporary frame list file
os.remove(frame_list_path)

print("Video rendering completed successfully.")
