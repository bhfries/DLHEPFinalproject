# run python MemeProcessor.py > BackgroundTweets.txt to create text file
# of english Background tweets

#Things I think I need
import json
import pandas as pd

tweets_data_path = '/Users/Alex/Documents/Data Science/Projects/Twitter Data Harvesting/Background.txt'

#Process JSON
tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

tweets = pd.DataFrame()

#Stick into DF as lists instead of maps
tweets['text'] = list(map(lambda tweet: tweet['text'], tweets_data))

#Filter by english tweets
english_tweets = tweets[tweets['lang'] == 'en']

#Print to file when called from terminal
print(english_tweets['text'])
