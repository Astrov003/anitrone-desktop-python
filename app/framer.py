import cv2
import numpy as np
import os

def sprites_to_frame(sprite1, sprite2):
    # Load images
    sprite_1 = cv2.imread(sprite1, cv2.IMREAD_UNCHANGED)
    sprite_1_glow = cv2.imread(sprite2, cv2.IMREAD_UNCHANGED)

    # Check if images have an alpha channel (transparency)
    if sprite_1 is None or sprite_1_glow is None:
        raise ValueError("Error loading images. Ensure the paths are correct.")

    if sprite_1.shape[2] != 4 or sprite_1_glow.shape[2] != 4:
        raise ValueError("Both images must be PNG files with an alpha channel.")

    # Initialize parameters
    total_frames = 30
    blend_duration = 200  # in ms for blending
    hold_duration = 200    # in ms for holding the blended image

    # Create output directory if it doesn't exist
    output_dir = './output'
    os.makedirs(output_dir, exist_ok=True)

    # Create a list to hold the frames
    frames = []

    # Calculate blending factors for 10 frames to fade in and fade out
    fade_in_frames = int(total_frames / 3)   # 10 frames for fade in
    hold_frames = int(total_frames / 3)       # 10 frames for hold
    fade_out_frames = int(total_frames / 3)   # 10 frames for fade out

    # Fade in
    for i in range(fade_in_frames):
        alpha = i / fade_in_frames
        blended_frame = cv2.addWeighted(sprite_1, 1 - alpha, sprite_1_glow, alpha, 0)
        frames.append(blended_frame)

    # Hold blended image
    for _ in range(hold_frames):
        frames.append(sprite_1_glow)

    # Fade out
    for i in range(fade_out_frames):
        alpha = (fade_out_frames - i) / fade_out_frames
        blended_frame = cv2.addWeighted(sprite_1, 1 - alpha, sprite_1_glow, alpha, 0)
        frames.append(blended_frame)

    # Save frames as PNGs
    for idx, frame in enumerate(frames):
        output_path = os.path.join(output_dir, f'frame_{idx:02d}.png')
        cv2.imwrite(output_path, frame)

    print(f"Frames generated and saved successfully in '{output_dir}'.")
