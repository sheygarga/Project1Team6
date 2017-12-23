import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

df=pd.read_csv('tweets_with_scores.csv')

def add_converted_time(df):
    time=[]
    for raw_time in df['tweet_created_at']:
        converted_time=datetime.strptime(raw_time, "%a %b %d %H:%M:%S %z %Y")
        time.append(converted_time)
    df['converted_time']=time
    df.sort_values(by=['converted_time'], inplace=True)
    return df

df=add_converted_time(df)

df_Ojai=df.loc[df['City']=='Ojai',:]
df_BH=df.loc[df['City']=='Beverly Hills',:]
df_Cre=df.loc[df['City']=='Crescenta',:]
df_LB=df.loc[df['City']=='Long_Beach',:]
df_SF=df.loc[df['City']=='San Fernando',:]
df_SB=df.loc[df['City']=='Santa Barbara',:]


city=['Ojai','Beverly Hills','Crescenta','Long Beach','San Fernando',
      'Santa Barbara']
values=[df_Ojai['compound'],df_BH['compound'],df_Cre['compound'],
        df_LB['compound'],df_SF['compound'],df_SB['compound']]

'''
fig,ax=plt.subplots()
ax.boxplot(values,labels=city)
ax.set_xticklabels(city, rotation=90)
'''

fig,ax=plt.subplots()
for i in range(6):
    dfi=df.loc[df['City']==city[i],:]
    ax.plot(dfi['converted_time'],dfi['compound'],'o',label=city[i])



ax.legend()
plt.show()
