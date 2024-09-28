from PIL import Image
import imageio
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Constants
def concat_final_videos(tempo, numOfElements):
    if tempo == 120:
        duration = 1  # Total duration for each APNG segment in seconds
    elif tempo == 150:
        duration = 0.8
    elif tempo == 180:
        duration = 0.6

    if numOfElements == 4:
        final_width = 880
    if numOfElements == 6:
        final_width = 1320
    if numOfElements == 8:
        final_width = 1760

    output_image_path = resource_path('output_image.png')
    apng_paths = [resource_path(f'image_{i}.png') for i in range(numOfElements)]  # Replace with your actual APNG filenames
    frame_rate = 30  # frames per second
    total_frames = int(frame_rate * duration)  # Total frames for each segment
    spatial_offset = 220  # Pixels offset to the right
    final_height = 220

    # Load the output image
    output_image = Image.open(output_image_path).convert("RGBA")
    final_frames = []

    # Create a blank image for final output
    blank_frame = Image.new("RGBA", (final_width, final_height))

    # Iterate through each APNG file
    for index, apng_path in enumerate(apng_paths):
        # Load the animated PNG
        apng = imageio.mimread(apng_path)
        
        # Resize each frame of the animated PNG to 220x220 pixels
        resized_frames = [Image.fromarray(frame).resize((220, 220), Image.ANTIALIAS) for frame in apng]
        
        # Calculate the x position for the current APNG
        x_offset = index * spatial_offset
        
        # Create frames for the final output
        for frame in resized_frames:
            # Create a new frame by pasting the output image and the current resized frame
            combined_frame = blank_frame.copy()
            combined_frame.paste(output_image, (0, 0), output_image)
            combined_frame.paste(frame, (x_offset, 0), frame)
            
            # Append the combined frame to final frames
            final_frames.append(combined_frame)

    # Calculate duration per frame in milliseconds
    frame_duration = (duration / total_frames) * 1000

    # Save the final animated PNG
    final_frames[0].save('final_output.png', save_all=True, append_images=final_frames[1:], loop=0, duration=int(frame_duration))
