#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3

import glob
from PIL import Image

# filepaths
fp_in = "plots/*.jpeg"
fp_out = "plots/results.gif"

# https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#gif
img, *imgs = [Image.open(f) for f in sorted(glob.glob(fp_in))]
img.save(fp=fp_out, format='GIF', append_images=imgs,
         save_all=True, duration=5000, loop=0)
