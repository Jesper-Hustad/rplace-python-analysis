import time
import pandas as pd
from datetime import datetime
from ast import literal_eval
import re
from PIL import Image
import math
import numpy as np
start_time = time.time()

# name = "2022_place_canvas_history.csv"
name = "canvas-01.csv"

it = iter(open(name, 'r'))

# skip headers
next(it)

def nextSection(date, offset):
     return pd.Timestamp(date) + pd.offsets.Minute(offset)
      

def generateDepthMap():
    canvas = np.full( (2000,2000),0)
    for i, val in enumerate(counts):
        if(val!=0):
            print("index", i, "for value", val)
        x = i%2000
        y = math.floor(i/2000)
        canvas[x,y] = val
    # img = Image.fromarray(np.uint8( canvas * (255/10) ) , 'L')
    # img.show()

def toCoordinates(line):
    quotesPos = line.find('"') + 1
    coord_string = line[quotesPos:-2]
    coords = re.sub(r'\b0+(?=[0-9])', '', coord_string)
    return literal_eval(coords)

length = 2000

counts = [0] * (2000**2)

section = pd.Timestamp(next(it)[:19])
section_minutes = 8
pos = 0

i = 0
j = 0
for line in it:

    x, y = toCoordinates(line)
    counts[y * 2000 + x] += 1

    date = pd.Timestamp(line[:19])

    # reached end of section
    if(date > section):
        print(line)
        section = nextSection(date, section_minutes)
        j += 1
        # if(j==2):
        generateDepthMap()
        counts = [0] * (2000**2)
    
    i += 1



# for i, val in enumerate(counts):
#     if(val!=0):
#         print("index", i, "for value", val)


# --------- DEBUGGING ---------
print(i, "lines")
seconds = time.time() - start_time
print(seconds, "seconds")
print(i / seconds, "lines/second")


