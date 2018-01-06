import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def add_scores(df):
    score_name=('compound','neg','pos','neu')
    score=([],[],[],[])
    for text in df['text']:
        vs=analyzer.polarity_scores(text)
        for i in range(len(score_name)):
            score[i].append(vs[score_name[i]])
    for i in range(len(score_name)):
        df[score_name[i]]=score[i]
    return df

analyzer = SentimentIntensityAnalyzer()

df=pd.read_csv('tweets2.csv')


features=['City','tweet_created_at','hashtags','text','screen_name','user_id',
              'user_created_at','user_friends_count','user_statuses_count',
              'tweet_id']

df=df.loc[:,features]


df=add_scores(df)

df.to_csv('tweets_with_scores2.csv')
