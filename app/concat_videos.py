from moviepy.editor import VideoFileClip, clips_array

# Define the number of videos and their paths
num_videos = 8
video_paths = [f"video_{i}.avi" for i in range(num_videos)]

# Load video clips
clips = [VideoFileClip(path) for path in video_paths]

# Set the canvas width and offset
canvas_width = 1760
offset = 220

# Create an empty list to hold the final clips with offset
final_clips = []

# Calculate the total width of the final layout
total_width = sum(clip.w for clip in clips) + (len(clips) - 1) * offset

# Resize clips to fit within the canvas width
resize_factor = canvas_width / total_width
resized_clips = [clip.resize(resize_factor) for clip in clips]

# Lay out the clips horizontally with offset
for i, clip in enumerate(resized_clips):
    final_clips.append(clip.set_position((i * (clip.w + offset), 0)))

# Create a final video by combining the clips
final_video = clips_array([final_clips])

# Write the final video to a file
final_video.write_videofile("final_video.mp4", codec='libx264', fps=24, audio=False)
