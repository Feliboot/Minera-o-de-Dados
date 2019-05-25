#import numpy as np
import pandas as pd
columns=['Seq._Name','mcg','gvh','lip','chg','aac','alm1','alm2','class']
df = pd.read_csv("ecoli.data",delim_whitespace=True,names = columns)
df.to_csv("ecoliSemColunas.csv",sep= ',',index= False)
