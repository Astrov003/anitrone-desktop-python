import os
from PIL import Image

# fix menu path when compiling to one file
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def create_image_canvas(tempo, numOfElements):
    
    # Define the folder containing your APNG files and the output image name
    apng_folder = ''  # Adjust this to your APNG folder path if needed
    output_image = resource_path('output_image.png')
    target_height = 220

    # Step 1: Extract the first frames from APNG
    first_frame_images = []
    for i in range(numOfElements):
        input_apng = resource_path(os.path.join(apng_folder, f'image_{i}.png'))
        
        # Open the APNG and get the first frame
        with Image.open(input_apng) as img:
            img.seek(0)  # Get the first frame
            first_frame = img.copy()  # Copy the first frame for processing
        
        # Resize the frame to the target height and maintain aspect ratio
        aspect_ratio = first_frame.width / first_frame.height
        new_width = int(target_height * aspect_ratio)
        
        # Resize the frame
        first_frame = first_frame.resize((new_width, target_height))
        first_frame_images.append(first_frame)

    # Step 2: Create a canvas to hold the combined image
    total_width = sum(image.width for image in first_frame_images)
    canvas = Image.new('RGBA', (total_width, target_height))

    # Step 3: Paste each frame onto the canvas
    current_x = 0
    for image in first_frame_images:
        canvas.paste(image, (current_x, 0))
        current_x += image.width

    # Step 4: Save the final image
    canvas.save(output_image)
    print("Canvas created and saved as", output_image)

