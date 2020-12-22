#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3

import glob
from PIL import Image
dev_t = 30
# filepaths
fp_in = "dev_run_{}/*.jpeg".format(dev_t)
fp_out = "dev_run_{}/results_normed_m1000_t200_dev{}.gif".format(dev_t, dev_t)

# https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#gif
img, *imgs = [Image.open(f) for f in sorted(glob.glob(fp_in))]
img.save(fp=fp_out, format='GIF', append_images=imgs,
         save_all=True, duration=50000, loop=0)
