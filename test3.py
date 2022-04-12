import time
import pandas as pd
from datetime import datetime

start_time = time.time()

section = "2022-04-04 00:58:00"
b= pd.Timestamp(section)

a = pd.Timestamp('2022-04-04 00:53:51')

# for i in range(10*6 * 50):
#     i = b-a

print((b>a))



seconds = time.time() - start_time

print(seconds, "seconds")