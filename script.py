from tabnanny import verbose
from types import coroutine
import pandas as pd
import matplotlib.colors
import numpy as np
from PIL import Image
from PIL import ImageColor
from ast import literal_eval
import numpy as np
import moviepy.editor as mpy



# canvas = np.full( (2000,2000,3), [255,255,255], dtype=np.uint8 )

canvas = np.zeros( (2000,2000,1))

# i = 0
# filename = "2022_place_canvas_history.csv"
filename = "2022_place_canvas_history-000000000000.csv"


data = pd.read_csv(filename)

val_counts = data["coordinate"].value_counts().to_frame()

print(val_counts)
print(val_counts["Value"])
val_counts.info(verbose=True)

val_counts = list(zip(*val_counts))

# row["pixel_color"] = row["pixel_color"].apply(lambda hex: ImageColor.getcolor(hex, "RGB")).apply(np.array)    

# print(val_counts[0])


coords = val_counts[0].apply(literal_eval).to_frame().apply(np.array)

print(coords)
# print(coords.info(verbose=True))
coords.info(verbose=True)

coords = list(zip(*coords))

print(coords)

canvas[coords[1], coords[0]] = [*val_counts[1].apply(np.array)]

# data['timestamp'] =  pd.to_datetime(data['timestamp'])

# for g in data.resample('10min', on='timestamp'):
# for g in data.groupby(['timestamp',pd.Grouper(freq='10min')]):

    # print(g)
# data = iter(data)


# csv_content = iter(pd.read_csv(filename, chunksize=10**6))

# for row in pd.read_csv(filename, chunksize=10**6):

# row = next(data)

# print(row)

def make_frame(t):
    print(t)


    # if(t%10 != 0):
    #     next(csv_content)
    #     return canvas

    
    
    row = next(csv_content)
    
    row["pixel_color"] = row["pixel_color"].apply(lambda hex: ImageColor.getcolor(hex, "RGB")).apply(np.array)    
    row['coordinate'] = row["coordinate"].apply(literal_eval).apply(np.array)
    
    coords = list(zip(*row["coordinate"]))

    canvas[coords[1], coords[0]] = [*row["pixel_color"]]

    return canvas


img = Image.fromarray(np.uint8(canvas / 1000) , 'L')
img.show()


# for i in range(5):
#     make_frame(i)

# if __name__ == '__main__':

#     clip = mpy.VideoClip(make_frame, duration=15.0)
#     clip.write_gif('ani.gif', fps=10)