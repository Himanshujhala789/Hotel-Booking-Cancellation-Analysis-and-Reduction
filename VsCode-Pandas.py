import pandas as pd
import numpy as np
dict1 = {"name":['Himanshu','Vivek','Shivam','Golu'],"marks":[10,20,30,40], "City":['Baran','Allahabad','Kota','Ajamgarh']}
df = pd.DataFrame(dict1)
df
df.to_csv('friends.csv')