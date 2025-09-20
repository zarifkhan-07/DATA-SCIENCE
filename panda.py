import pandas as pd
import numpy as np

dataset={'name':['Jonny','Tommy','Zarif','Jimmy','Noob','Isac','Montasir','Rauf','Tom','Jhon'],
         'score':[23,     34,     100,    np.nan, 2,     99,    89,        2.4,   55.9, 99.9 ],
         'attempts':[ 2,      5,      1,     40,  1222,     1,         3,    91,    3,     9 ],
         'qualify': ['NO', 'NO',  'YES',  'NO',   'NO',  'YES', 'YES',     'NO',  'NO', 'YES']}

label=['a','b','c','d','e','f','g','h','i','j']

df=pd.DataFrame(dataset,index=label)
print("INFO:")
print(df.info())