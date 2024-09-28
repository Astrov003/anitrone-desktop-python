import os
import shutil

def clean_up_files():
  for i in range(8):
    filename = f"image_{i}.png"
    os.remove(filename)

  shutil.rmtree('output')
  os.remove('output_image.png')
  