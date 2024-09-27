import os
import subprocess

# Constants
frame_width = 220
frame_height = 220
num_frames_per_group = 30
num_groups = 8
total_width = frame_width * num_groups  # 1760px
output_video_path = 'output_video.mov'  # Change the output video format to .mov
frame_folder = '../output'  # Change this to your folder path

# Create a temporary file to hold the frame information for each group
temp_video_paths = []

for group in range(num_groups):
    temp_video_path = f'video_{group}.avi'
    temp_video_paths.append(temp_video_path)

    # Create a temporary file to hold the frame information for the current group
    frame_list_path = f'frames_group_{group}.txt'

    # Prepare the list of frames for the current group
    with open(frame_list_path, 'w') as f:
        for frame_index in range(num_frames_per_group):
            global_index = group * num_frames_per_group + frame_index
            frame_path = os.path.join(frame_folder, f'frame_{global_index}.png')  # Ensure your frames have an alpha channel
            
            if os.path.exists(frame_path):
                f.write(f"file '{frame_path}'\n")
                f.write(f"duration 0.03333\n")  # Duration for each frame (30 FPS)
            else:
                print(f"Warning: Frame {frame_path} not found.")

    # Run ffmpeg to create a video for the current group
    subprocess.run([
        'ffmpeg',
        '-y',  # Overwrite output files
        '-f', 'concat',  # Use concat demuxer
        '-safe', '0',  # Allow unsafe file paths
        '-i', frame_list_path,  # Input the list of frames
        '-c:v', 'png',  # Use PNG codec for lossless video
        '-pix_fmt', 'yuva420p',  # Set pixel format to include alpha channel
        temp_video_path
    ])

    # Clean up the temporary frame list file
    os.remove(frame_list_path)

# Now concatenate all the temporary videos into the final video
# concat_filter = '|'.join(temp_video_paths)
# subprocess.run([
#     'ffmpeg',
#     '-y',  # Overwrite output files
#     '-i', f'concat:{concat_filter}',  # Concatenate the temporary videos
#     '-c:v', 'png',  # Use PNG codec for lossless video
#     '-pix_fmt', 'yuva420p',  # Set pixel format to include alpha channel
#     output_video_path
# ])

# # Clean up the temporary video files
# for temp_video in temp_video_paths:
#     os.remove(temp_video)

print("Video rendering completed successfully.")
