import os
import shutil

def clean_up_files(numOfElements):
  for i in range(numOfElements):
    filename = f"image_{i}.png"
    os.remove(filename)

  shutil.rmtree('output')
  os.remove('output_image.png')
  