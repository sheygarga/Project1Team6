import pandas as pd

city='Santa_Barbara.csv'

name=['2','3','4','5','6','7','8','9','10']

df=pd.read_csv('1')

for i in range(9):
    df_add=pd.read_csv(name[i])
    df=pd.concat([df,df_add],ignore_index=True)

df.drop_duplicates()

df.to_csv(city)

print(df.shape)


features=['City','tweet_created_at','hashtags','text','screen_name','user_id',
              'user_created_at','user_friends_count','user_statuses_count',
              'tweet_id']

df=pd.read_csv(city)
df=df.loc[:,features]
df.to_csv(city)
