import numpy as np
import moviepy.editor as mpy

def make_frame(t):

    h = 100
    w = 100

    ar = np.zeros((h, w, 3))

    for hi in range(h):
        for wi in range(w):
            for ci in range(3):
                ar[hi, wi, ci] = 255.0*t/15.0
    return ar


if __name__ == '__main__':

    clip = mpy.VideoClip(make_frame, duration=15.0)
    clip.write_gif('ani.gif', fps=15)