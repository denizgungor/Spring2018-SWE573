import tweepy
from tweepy import cursor
from tweepy import API
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

consumer_key = '87VYrYX0L5FrfvjMiPexwQgZG'
consumer_secret = 'RdFqHfksr0AxLhZLG8UtAntqPbbFsAY1dNP7SUMYXvFWrjHtsp'
access_token = '87045682-PmvV1Vsoh3Ptmyx2vIljXNZBs4CQmrkMEpYnHLwGn'
access_token_secret = 'bXzldHQuuym7BBvuUREQcp8yFehrsveZjBNpIfkZpf8VO'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


def process_status(s):
    print(s)


# Iterate through the first 200 statuses in the friends timeline
#for friend in tweepy.API(   )
    # Process the status here
 #   process_status(friend)





results = api.search(q="Huawei", count=100, lang='en')

for tweet in tweepy.Cursor(api.search,
                       q="HUAWEI",
                       count=100,
                       result_type="recent",
                       include_entities=True,
                       lang="en").items():
    print(tweet.text
          )


#for page in tweepy.Cursor().pages():
#    print(page)


#for result in results:
    #print(result.text)
    #print(result.user)

#sid = SentimentIntensityAnalyzer()
#f#or sentence in results:
#     print(sentence.text)
#     ss = sid.polarity_scores(sentence.text)
#     for k in ss:
#         print('{0}: {1}, '.format(k, ss[k]), end='')
 #    print()