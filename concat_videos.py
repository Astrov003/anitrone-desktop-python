import sys
from PIL import Image
import imageio
import os
import tkinter as tk
from tkinter import filedialog
from datetime import datetime

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
        duration_factor = 1  # Speed factor for each APNG segment
    elif tempo == 150:
        duration_factor = 0.8
    elif tempo == 180:
        duration_factor = 0.6

    if numOfElements == 4:
        final_width = 880
    elif numOfElements == 6:
        final_width = 1320
    elif numOfElements == 8:
        final_width = 1760

    output_image_path = 'output_image.png'
    apng_paths = [f'image_{i}.png' for i in range(numOfElements)]  # Replace with your actual APNG filenames

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
        apng = imageio.mimread(apng_path, memtest=False)
        
        # Get original duration for each frame
        meta_data = imageio.get_reader(apng_path).get_meta_data()
        original_duration = meta_data.get('duration', 100)  # Default duration in milliseconds
        
        # Double the speed by halving the duration
        new_duration = original_duration / 2  # Make it run twice as fast
        
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

    # Create a Tkinter root window (needed for the file dialog)
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Get current datetime for placeholder in the filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    default_filename = f"Ani_{timestamp}.png"

    # Show a save dialog
    save_path = filedialog.asksaveasfilename(
        title="Save Final Animated PNG",
        defaultextension=".png",
        filetypes=[("PNG files", "*.png")],
        initialfile=default_filename
    )

    # If the user selects a file, save the animated PNG
    if save_path:
        final_frames[0].save(
            save_path, 
            save_all=True, 
            append_images=final_frames[1:], 
            duration=50,  # Use the halved duration
            loop=0
        )

    root.destroy()  # Close the Tkinter root window
