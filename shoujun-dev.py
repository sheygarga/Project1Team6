import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tweepy
import json
import time

def show_tweet(tweet):
    return json.dumps(tweet, indent=4)
    

consumer_key='sP7RxK8b1MI2jSz0oG4d0jvNW'
consumer_secret='EUjv07IfT5d0sLaRAvG9qBgSew4xQheIwNMQbdHFe8mYZtQsyn'
access_token='104740161-HT4boK0Fyh352PWdzaEtjaZILNJI3DEMm0sYLtMY'
access_token_secret='8yMWItCYF4c082dyRbUepSeM14X5ZW3jAbh66XMSgtzBE'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,parser=tweepy.parsers.JSONParser())

def tweets_to_csv(tweets,city='Ojai',filename='tweets.csv'):
    tweets=tweets.get('statuses')
    features=['City','tweet_created_at','hashtags','text','screen_name','user_id',
              'user_created_at','user_friends_count','user_statuses_count',
              'tweet_id']
    data_list=[[],[],[],[],[],[],[],[],[],[]]
    if tweets:
        for tweet in tweets:
            data_list[0].append(city)
            data_list[1].append(tweet.get('created_at'))
            data_list[2].append(tweet.get('entities').get('hashtags'))  
            data_list[3].append(tweet.get('text'))
            data_list[4].append(tweet.get('user').get('screen_name'))
            data_list[5].append(tweet.get('user').get('id'))
            data_list[6].append(tweet.get('user').get('created_at'))
            data_list[7].append(tweet.get('user').get('friends_count'))
            data_list[8].append(tweet.get('user').get('statuses_count'))
            data_list[9].append(tweet.get('id'))
        df=pd.DataFrame({features[i]:data_list[i] for i in range(10)})
        df.loc[:,features].to_csv(filename)
        max_id=df.tail(1)['tweet_id'].reset_index(drop=True)[0]
        return_message='Tweets info is written to file: {}'.format(filename)
        print(return_message)
        return max_id
    else:
        print('No Tweets found.')
        return None



lat='34.421450'
long='-119.716562'
city='Santa Barbara'


tweets=api.search(q='Thomas fire', lang='en',lat=lat,long=long,accuracy='17km',
             count=100)

max_id=tweets_to_csv(tweets,city=city, filename='1')

num=2
label=str(num)

for i in range(9):
    tweets=api.search(q='Thomas fire', lang='en',lat=lat,long=long,accuracy='17km',
             count=100, max_id=max_id)
    max_id=tweets_to_csv(tweets, city=city, filename=label)
    num+=1
    label=str(num)
    time.sleep(10)



