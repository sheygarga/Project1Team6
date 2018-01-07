import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pylab import setp

df=pd.read_csv('tweets_sentiment.csv')

c1=df.loc[df['City']=='Ojai',['compound']].values
c2=df.loc[df['City']=='San Fernando',['compound']].values
c3=df.loc[df['City']=='Beverly Hills',['compound']].values
c4=df.loc[df['City']=='La Crescenta',['compound']].values
c5=df.loc[df['City']=='Long Beach',['compound']].values
c6=df.loc[df['City']=='Santa Barbara',['compound']].values

p1=df.loc[df['City']=='Ojai',['pos']].values
p2=df.loc[df['City']=='San Fernando',['pos']].values
p3=df.loc[df['City']=='Beverly Hills',['pos']].values
p4=df.loc[df['City']=='La Crescenta',['pos']].values
p5=df.loc[df['City']=='Long Beach',['pos']].values
p6=df.loc[df['City']=='Santa Barbara',['pos']].values

n1=df.loc[df['City']=='Ojai',['neg']].values
n2=df.loc[df['City']=='San Fernando',['neg']].values
n3=df.loc[df['City']=='Beverly Hills',['neg']].values
n4=df.loc[df['City']=='La Crescenta',['neg']].values
n5=df.loc[df['City']=='Long Beach',['neg']].values
n6=df.loc[df['City']=='Santa Barbara',['neg']].values

u1=df.loc[df['City']=='Ojai',['neu']].values
u2=df.loc[df['City']=='San Fernando',['neu']].values
u3=df.loc[df['City']=='Beverly Hills',['neu']].values
u4=df.loc[df['City']=='La Crescenta',['neu']].values
u5=df.loc[df['City']=='Long Beach',['neu']].values
u6=df.loc[df['City']=='Santa Barbara',['neu']].values

d1=[c1,c2,c3,c4,c5,c6]
d2=[p1,p2,p3,p4,p5,p6]
d3=[n1,n2,n3,n4,n5,n6]
d4=[u1,u2,u3,u4,u5,u6]


colors = ['grey', 'lightgreen','red', 'lightblue']
clabels=['Compound','Pos','Neg','Neu']

labels=['Ojai','San Fernando','Beverly Hills','La Crescenta','Long Beach',
        'Santa Barbara']

print(type(c1))


fig,ax=plt.subplots(figsize=(10,10))

bp1=ax.boxplot(d1,positions=[1,7,13,19,25,31], widths=0.6,patch_artist=True)
for box in bp1['boxes']:
    box.set(color='grey',linewidth=2)

bp2=ax.boxplot(d2,positions=[2,8,14,20,26,32], widths=0.6,patch_artist=True)
for box in bp2['boxes']:
    box.set(color='lightgreen',linewidth=2)

bp3=ax.boxplot(d3,positions=[3,9,15,21,27,33], widths=0.6,patch_artist=True)
for box in bp3['boxes']:
    box.set(color='red',linewidth=2)

bp4=ax.boxplot(d4,positions=[4,10,16,22,28,34], widths=0.6,patch_artist=True)
for box in bp4['boxes']:
    box.set(color='lightblue',linewidth=2)

ax.set_title('Sentiment Analysis of Different Cities')
ax.set_xbound(lower=0,upper=45)
ax.set_xticks(np.linspace(2,33,6))

ax.set_xticklabels(labels,rotation=45)

for i in range(4):
    ax.plot([],color=colors[i],label=clabels[i])

ax.legend()

plt.savefig('sen_analysis.png')
plt.clf()
