import pandas as pd

df1=pd.read_csv('Ojai.csv')
df2=pd.read_csv('Beverly_Hills.csv')
df3=pd.read_csv('Crescenta.csv')
df4=pd.read_csv('Long_Beach.csv')
df5=pd.read_csv('San_Fernando.csv')
df6=pd.read_csv('Santa_Barbara.csv')

df=pd.concat([df1,df2,df3,df4,df5,df6],ignore_index=True)

df.to_csv('tweets2.csv')
