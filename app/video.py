import cv2
import os
import numpy as np

# Constants
frame_width = 220
frame_height = 220
num_frames_per_group = 30
num_groups = 8
total_width = frame_width * num_groups  # 1760px
output_video_path = 'output_video.mp4'
frame_folder = '../output'  # Change this to your folder path

# Create a video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter(output_video_path, fourcc, 30.0, (total_width, frame_height))

# Process each group
for group in range(num_groups):
    # Create a blank image for the group
    group_image = np.zeros((frame_height, total_width, 3), dtype=np.uint8)

    # Read and process frames in the current group
    for frame_index in range(num_frames_per_group):
        # Calculate the global index of the frame
        global_index = group * num_frames_per_group + frame_index
        frame_path = os.path.join(frame_folder, f'frame_{global_index}.png')  # Adjust the file extension if needed
        frame = cv2.imread(frame_path)

        if frame is not None:
            # Resize the frame
            resized_frame = cv2.resize(frame, (frame_width, frame_height))
            x_offset = group * frame_width
            group_image[:, x_offset:x_offset + frame_width] = resized_frame
        else:
            print(f"Warning: Frame {frame_path} not found.")

        video_writer.write(group_image)

# Release the video writer
video_writer.release()

print("Video rendering completed successfully.")
