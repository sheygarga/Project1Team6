import pandas as pd


df1=pd.read_csv('tweets_with_scores.csv')
df2=pd.read_csv('tweets_with_scores2.csv')


df=pd.concat([df1,df2],ignore_index=True)
df=df.sort_values(by=['City'])

df.to_csv('combined_tweets.csv')

