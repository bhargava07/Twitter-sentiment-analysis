i#importing the required libraries
import pandas as pd     # For data manipulation and analysis
import numpy as np      # For Scientific computing
import tweepy           # For Accessing Twitter's API
import matplotlib.pyplot as plt    # For plotting and visualization:
import random

#Loading twitter consumer and access token's
consumer_key = ""
comsumer_secret = ""
access_token = ""
access_secret = ""

#Authentication of consumer and access token's
from credentials import *    # This will allow us to use the keys as variables

#Creating Twitter_api_call function:
def twitter_api_call():
    """
    This function is used to setup the Twitter's API
    with our consumer and access keys provided.
    """
  # Authentication and access using keys:
    auth = tweepy.OAuthHandler(consumer_key, comsumer_secret)
    auth.set_access_token(access_token, access_secret)

    # Return API with authentication:
    api = tweepy.API(auth)
    return api

#Creating an api_call object:
api_call = twitter_api_call()

# Twitter list is been created:
tweets = api_call.user_timeline(screen_name="@elonmusk", count=200)
print("Number of tweets extracted: {}.\n".format(len(tweets)))

#Printing the most recent 10 tweets:
print("10 recent tweets:\n")
for tweet in tweets[:10]:
    print(tweet.text)
    print()

#Creating a dataframe 
data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])

#displaying the first 10 columns
data.head(10)

#displaying the internal methods of the object 
print(dir(tweets[0]))

#creating new columns in our dataframe
data['len']  = np.array([len(tweet.text) for tweet in tweets])
data['ID']   = np.array([tweet.id for tweet in tweets])
data['Source'] = np.array([tweet.source for tweet in tweets])
data['Likes']  = np.array([tweet.favorite_count for tweet in tweets])
data['ReTweets']    = np.array([tweet.retweet_count for tweet in tweets])
display(data.head(10))
#importing the libraries
from textblob import TextBlob
import re

#creating a text_cleaning function 
def text_cleaning(tweet):
    '''
    This function is used to clean the text in a tweet by removing 
    links and special characters using regex.
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

#creating a sentiment function
def sentiment(tweet):
    '''
    This function is used to classify the polarity of a tweet
    using textblob.
    '''
    analysis = TextBlob(text_cleaning(tweet))
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity == 0:
        return "Neutral"
    else:
        return "Negative"

#Creating a sentiment_analysis column:
data['Sentiment_Analysis'] = np.array([ sentiment(tweet) for tweet in data['Tweets'] ])

#Displaying the dataframe with the sentiment_analysis column:
display(data.head(10))

#Displaying the tweets which has more number of likes and retweets
Max_likes = np.max(data['Likes'])
Max_reTweets  = np.max(data['ReTweets'])

likes = data[data.Likes == Max_likes].index[0]
retweets = data[data.ReTweets == Max_reTweets].index[0]

# Max Likes:
print("The tweet with more likes is: \n{}".format(data['Tweets'][likes]))
print("Number of likes: {}".format(Max_likes))
print("{} characters.\n".format(data['len'][likes]))

# Max ReTweets:
print("The tweet with more retweets is: \n{}".format(data['Tweets'][retweets]))
print("Number of retweets: {}".format(Max_reTweets))
print("{} characters.\n".format(data['len'][retweets]))

#displaying the count of postive,negative and neutral tweets
data["Sentiment_Analysis"].value_counts()

#plotting a graph for the sentiment analysis  
data["Sentiment_Analysis"].value_counts().plot.bar()
#importing the required libraries
import pandas as pd     # For data manipulation and analysis
import numpy as np      # For Scientific computing
import tweepy           # For Accessing Twitter's API
import matplotlib.pyplot as plt    # For plotting and visualization:

#Loading twitter consumer and access token's
consumer_key = ""
comsumer_secret = ""
access_token = ""
access_secret = ""

#Authentication of consumer and access token's
from credentials import *    # This will allow us to use the keys as variables

#Creating Twitter_api_call function:
def twitter_api_call():
    """
    This function is used to setup the Twitter's API
    with our consumer and access keys provided.
    """
  # Authentication and access using keys:
    auth = tweepy.OAuthHandler(consumer_key, comsumer_secret)
    auth.set_access_token(access_token, access_secret)

    # Return API with authentication:
    api = tweepy.API(auth)
    return api

#Creating an api_call object:
api_call = twitter_api_call()

# Twitter list is been created:
tweets = api_call.user_timeline(screen_name="@elonmusk", count=200)
print("Number of tweets extracted: {}.\n".format(len(tweets)))

#Printing the most recent 10 tweets:
print("10 recent tweets:\n")
for tweet in tweets[:10]:
    print(tweet.text)
    print()

#Creating a dataframe 
data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])

#displaying the first 10 columns
data.head(10)

#displaying the internal methods of the object 
print(dir(tweets[0]))

#creating new columns in our dataframe
data['len']  = np.array([len(tweet.text) for tweet in tweets])
data['ID']   = np.array([tweet.id for tweet in tweets])
data['Source'] = np.array([tweet.source for tweet in tweets])
data['Likes']  = np.array([tweet.favorite_count for tweet in tweets])
data['ReTweets']    = np.array([tweet.retweet_count for tweet in tweets])
display(data.head(10))
#importing the libraries
from textblob import TextBlob
import re

#creating a text_cleaning function 
def text_cleaning(tweet):
    '''
    This function is used to clean the text in a tweet by removing 
    links and special characters using regex.
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

#creating a sentiment function
def sentiment(tweet):
    '''
    This function is used to classify the polarity of a tweet
    using textblob.
    '''
    analysis = TextBlob(text_cleaning(tweet))
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity == 0:
        return "Neutral"
    else:
        return "Negative"

#Creating a sentiment_analysis column:
data['Sentiment_Analysis'] = np.array([ sentiment(tweet) for tweet in data['Tweets'] ])

#Displaying the dataframe with the sentiment_analysis column:
display(data.head(10))

#Displaying the tweets which has more number of likes and retweets
Max_likes = np.max(data['Likes'])
Max_reTweets  = np.max(data['ReTweets'])

likes = data[data.Likes == Max_likes].index[0]
retweets = data[data.ReTweets == Max_reTweets].index[0]

# Max Likes:
print("The tweet with more likes is: \n{}".format(data['Tweets'][likes]))
print("Number of likes: {}".format(Max_likes))
print("{} characters.\n".format(data['len'][likes]))

# Max ReTweets:
print("The tweet with more retweets is: \n{}".format(data['Tweets'][retweets]))
print("Number of retweets: {}".format(Max_reTweets))
print("{} characters.\n".format(data['len'][retweets]))

#displaying the count of postive,negative and neutral tweets
data["Sentiment_Analysis"].value_counts()

#plotting a graph for the sentiment analysis  
data["Sentiment_Analysis"].value_counts().plot.bar()
