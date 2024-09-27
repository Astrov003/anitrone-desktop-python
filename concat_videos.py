from moviepy.editor import ImageClip, VideoFileClip, CompositeVideoClip, clips_array
import os

def concat_final_videos(tempo):
    if tempo == 120:
        duration = 8
        frames = 30
    elif tempo == 150:
        duration = 6.4
        frames = 24
    elif tempo == 180:
        duration = 5.35
        frames = 20
        
    # Define the number of images and their paths
    num_images = 8
    image_paths = [f"image_{i}.png" for i in range(num_images)]  # Change to PNG files

    # Load image clips
    clips = [ImageClip(path).set_duration(duration) for path in image_paths]

    # Set the canvas width and offset
    canvas_width = 1760
    offset = 220
    frame_rate = 30
    frame_offset = frames / frame_rate
    clip_size = (220, 220)

    # Create an empty list to hold the final clips with offset
    final_clips = []

    # Calculate the total width of the final layout
    total_width = sum(clip.size[0] for clip in clips) + (len(clips) - 1) * offset

    # Resize clips to fit within the canvas width
    resize_factor = canvas_width / total_width
    resized_clips = [clip.resize(resize_factor) for clip in clips]

    # Lay out the clips horizontally with offset
    for i, clip in enumerate(resized_clips):
        resized_clip = clip.resize(clip_size)
        start_time = i * frame_offset  # Set start time for each clip
        final_clips.append(resized_clip.set_start(start_time).set_position((i * (clip_size[0]), 0)))

    # Create a final video by combining the clips
    final_video = clips_array([final_clips])

    # Load the existing video if needed
    existing_video_path = "output_video.mp4"  # Update with your existing video path
    
    # Check if the existing video is a valid video file
    existing_video = None
    if os.path.exists(existing_video_path):
        if existing_video_path.endswith(('.mp4', '.avi', '.mov', '.mkv')):  # Check for common video formats
            existing_video = VideoFileClip(existing_video_path).set_duration(duration)
    
    # Create a composite video with the final video on top of the existing video, if it exists
    if existing_video:
        output_video = CompositeVideoClip([existing_video, final_video.set_position((0, 0))])
    else:
        output_video = final_video

    # Write the final video to a file
    output_video.write_videofile("combined_final_video.mp4", codec='libx264', fps=30, audio=False)

