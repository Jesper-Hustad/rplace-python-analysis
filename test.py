import pandas as pd
import numpy as np
from PIL import Image
from PIL import ImageColor
from ast import literal_eval
import numpy as np
import moviepy.editor as mpy
from IPython.display import display, HTML
from tqdm import tqdm
import wget
import gzip
import os
import dask.dataframe as dd
from pandas.tseries.offsets import DateOffset

# import numpy as np
# import moviepy.editor as mpy

# def make_frame(t):

#     h = 100
#     w = 100

#     ar = np.zeros((h, w, 3))

#     for hi in range(h):
#         for wi in range(w):
#             for ci in range(3):
#                 ar[hi, wi, ci] = 255.0*t/15.0
#     return ar


# if __name__ == '__main__':

#     clip = mpy.VideoClip(make_frame, duration=15.0)
#     clip.write_gif('ani.gif', fps=15)

# loops = 10**6 * 90
# n = 0

# for i in range(loops):
#     n += 1

# print(n)

canvas = np.full( (2000,2000),50)

img = Image.fromarray(np.uint8( canvas * (255/100) ) , 'L')
img.show()