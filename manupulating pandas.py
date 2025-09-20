import pandas as pd
import numpy as np


data={'Name':['Pankaj','Meghna','David','Lisa'],
      'Role':['CEO', np.nan, np.nan, np.nan],
      'Salary':[1200, 300, np.nan, np.nan]}
label=[1,2,3,4]

df=pd.DataFrame(data,index=label)
print("INFO:\n",df)
print(df.info())