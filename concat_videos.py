from moviepy.editor import VideoFileClip, CompositeVideoClip, clips_array
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
        
    # Define the number of videos and their paths
    num_videos = 8
    video_paths = [f"video_{i}.avi" for i in range(num_videos)]

    # Load video clips
    clips = [VideoFileClip(path) for path in video_paths]

    # Set the canvas width and offset
    canvas_width = 1760
    offset = 220
    frame_rate = 30
    frame_offset = frames / frame_rate
    clip_size = (220, 220)

    # Create an empty list to hold the final clips with offset
    final_clips = []

    # Calculate the total width of the final layout
    total_width = sum(clip.w for clip in clips) + (len(clips) - 1) * offset

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

    # Load the existing video
    existing_video_path = "output_video.mp4"  # Update with your existing video path
    existing_video = VideoFileClip(existing_video_path)

    # Create a composite video with the final video on top of the existing video
    output_video = CompositeVideoClip([existing_video, final_video.set_position((0, 0))])

    # Write the final video to a file
    output_video.write_videofile("combined_final_video.mp4", codec='libx264', fps=30, audio=False)
