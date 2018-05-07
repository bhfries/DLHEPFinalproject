#Run python BackgroundHarvestor.py > FileName.txt in terminal and let run until quantity satisfied
#Keyword filter at bottom
#Things I think we need
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Account created and access info
access_token = "854085236-EuXLiVBtL8txA1m7qbzpvw5SWnNrg3tI0HCLyc7h"
access_token_secret = "pGjJkZOd7y2nkQim401WUhlLwsHzkcSKSt3KH5u5W5nyK"
consumer_key = "KZSmj4904W5KrhYb0jr1jTNrs"
consumer_secret = "KIPFzApbSpy78a9xIxQ7yhgk62NkgjE7Q4oCQ1iCATK4Pwowax"


#Tweepy listener prints out to system
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_status(self, status):
        print('full_text:', status.extended_tweet['full_text'])

#Connects to Twitter API
if __name__ == '__main__':

    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l, tweet_mode='extended') #necessary tweet_mode param to get full text

    #Filter by keywords
    stream.filter(track=['#DeepLearning', '#MachineLearning',
                         '#ArtificialIntelligence', 'Neural Networks'])
