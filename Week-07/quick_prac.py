import numpy as np
import pandas as pd

temp = pd.Series([10,20,30,20,np.nan])
print(temp)
print("_______________________")
print(temp.sum())
print("_______________________")
print(temp.mean())
print("_______________________")
print(temp.max())
print("_______________________")
print(temp.min())
print("_______________________")
print(temp.head(3))
#head values
print("_______________________")
print(temp.isnull())
#Bool if nan is found
print("_______________________")
temp = temp.fillna(0)
print(temp)
#Fills NaN
print("_______________________")
print(temp.sort_values())
#sorts the series
print("_______________________")
print(temp.value_counts())
#Counts number of times a value appears
print("_______________________")


