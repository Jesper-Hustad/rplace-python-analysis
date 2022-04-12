
import pandas as pd

a = pd.Categorical([1,2])

a.insert(1, 3)

print(a)