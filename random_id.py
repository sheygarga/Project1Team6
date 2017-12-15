import random
import tweepy
import json

def show_tweet(tweet):
    return json.dumps(tweet, indent=4)

def random_word(): #https://github.com/dwyl/english-words
    with open('words_alpha.txt', 'r') as f:
        words=f.read().split('\n')
        return random.choice(words)

def get_random_user(loc=None):
    word=random_word()
    tweets=api.search(q=word, rpp=100, count=1000)
    count=tweets.get("search_metadata").get("count")
    index=random.randint(1,count)
    if tweets.get("statuses"):
        user_id=tweets.get("statuses")[index-1].get('user').get('id')
    else:
        return None
    return user_id


#Set params
consumer_key=
consumer_secret=
access_token=
access_token_secret=

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,parser=tweepy.parsers.JSONParser())


#Get random user
test=get_random_user()
print(test)
