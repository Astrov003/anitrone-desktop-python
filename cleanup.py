import os
import shutil

def clean_up_files():
  for i in range(8):
    filename = f"video_{i}.avi"
    os.remove(filename)

  shutil.rmtree('output')
  os.remove('output_video.mp4')
  