import pandas as pd

def tweets_to_csv(tweets, filename='tweets.csv'):
    tweets=tweets.get('statuses')
    features=['tweet_created_at','hashtags','text','screen_name','user_id',
              'user_created_at','user_friends_count','user_statuses_count']
    data_list=([],[],[],[],[],[],[],[])
    if tweets:
        for tweet in tweets:
            data_list[0].append(tweet.get('created_at'))
            data_list[1].append(tweet.get('entities').get('hashtags'))  
            data_list[2].append(tweet.get('text'))
            data_list[3].append(tweet.get('user').get('screen_name'))
            data_list[4].append(tweet.get('user').get('id'))
            data_list[5].append(tweet.get('user').get('created_at'))
            data_list[6].append(tweet.get('user').get('friends_count'))
            data_list[7].append(tweet.get('user').get('statuses_count'))
        df=pd.DataFrame({features[i]:data_list[i] for i in range(8)})
        df.loc[:,features].to_csv(filename)
        return_message='Tweets info is written to file: {}'.format(filename)
        print(return_message)
        return len(tweets)
    else:
        print('No Tweets found.')
        return None 
    
