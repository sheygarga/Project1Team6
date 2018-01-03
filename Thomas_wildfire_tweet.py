
# coding: utf-8

# In[2]:

# Dependencies
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import tweepy
import time
import seaborn as sns

# Initialize Sentiment Analyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

# Twitter API Keys
consumer_key = "Ed4RNulN1lp7AbOooHa9STCoU"
consumer_secret = "P7cUJlmJZq0VaCY0Jg7COliwQqzK0qYEyUF9Y0idx4ujb3ZlW5"
access_token = "839621358724198402-dzdOsx2WWHrSuBwyNUiqSEnTivHozAZ"
access_token_secret = "dCZ80uNRbFDjxdU2EckmNiSckdoATach6Q8zb7YYYE5ER"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# In[3]:

thomFire_tweet=api.search('#thomasfire',
                          lat='34.407365',long=' -119.081787',accuracy='17km',
                          count=100,
                          truncate=False,
                          since='2017-12-01', until='2017-12-16')
#                           min_id='Thu Dec 14 15:29:45 +0000 2017',
#                           until= '2017-12-11')#Thu Dec 7 15:29:45 +0000 2017',
#                           created_at='Thu Dec 14 15:29:45 +0000 2017',
#                           result_type="old"



# In[4]:

thomFire_tweet


# In[5]:

for tweet in tweepy.Cursor(api.search,q='%20thomasfire',
                          lat='34.407365',long=' -119.081787',accuracy='17km',
                          count=100,
                          truncate=False,
                          until= '2017-12-11').items():
    # process status here
    tweet_date.append(thomFire_tweet['statuses'] #['search_metadata']#['created_at']


# In[23]:

tweet_date=[]
for i in range (99):
    tweet_date.append(thomFire_tweet['statuses'][i] ['created_at'] )#['search_metadata']#['created_at']
    
t=pd.DataFrame(tweet_date, columns=['dtb'])
t['dty']=(t.dtb.str.slice(start=0,stop=11))
t.dty.value_counts()


# In[22]:


# Variables for holding sentiments
compound_list = []
positive_list = []
negative_list = []
neutral_list = []

# Loop through 75 pages of tweets (total 1500 tweets)
for page in tweepy.Cursor(api.search,'#thomasfire',
                  lat='34.407365',long=' -119.081787',accuracy='17km',
                  count=100,
                  truncate=False,
#                   since='2017-12-01', until='2017-12-16').pages(75):

    # Get all tweets from home feed
#     page_all = store_tweets(page['statuses'],file='tweets.json')
    page = page[0]
    tweet = json.dumps(page._json(),indent=3)
    tweet = json.loads(tweet)
    text = tweet['text']

    # Run Vader Analysis on each tweet
    compound = analyzer.polarity_scores(text)["compound"]
    pos = analyzer.polarity_scores(text)["pos"]
    neu = analyzer.polarity_scores(text)["neu"]
    neg = analyzer.polarity_scores(text)["neg"]

    # Add each value to the appropriate array
    compound_list.append(compound)
    positive_list.append(pos)
    negative_list.append(neg)
    neutral_list.append(neu)

    # Print the Averages for each user
    print("")
    print("User: %s" % user)
    print("Compound: %s" % np.mean(positive_list))
    print("Positive: %s" % np.mean(positive_list))
    print("Neutral: %s" % np.mean(neutral_list))
    print("Negative: %s" % np.mean(negative_list))

    
#     # Run Vader Analysis on each tweet
#     compound = analyzer.polarity_scores(tweet["text"])["compound"]
#     pos = analyzer.polarity_scores(tweet["text"])["pos"]
#     neu = analyzer.polarity_scores(tweet["text"])["neu"]
#     neg = analyzer.polarity_scores(tweet["text"])["neg"]
#     tweets_ago = counter

#     # Add sentiments for each tweet into an array
#     sentiments.append({"Date": tweet["created_at"], 
#                        "Compound": compound,
#                        "Positive": pos,
#                        "Negative": neu,
#                        "Neutral": neg,
#                        "Tweets Ago": counter})

#     # Add to counter 
#     counter = counter + 1


#     # Only iterate through the first 200 statuses
# for status in tweepy.Cursor(api.user_timeline).items(200):
#     process_status(status)

# # Only iterate through the first 3 pages
# for page in tweepy.Cursor(api.user_timeline).pages(3):
#     process_page(page)


# In[1]:

thomas_tweet

