import tweepy
from keys import *


client = tweepy.Client(bearer_token)

# client = tweepy.Client(
#     bearer_token=bearer_token,
#     consumer_key=consumer_key,
#     consumer_secret=consumer_secret,
#     access_token=access_token,
#     access_token_secret=access_token_secret,
# )


username = input('Enter a tweeter ID : ')

user = client.get_user(username=username)
user_id = user[0].id

try:
    followers = len(client.get_users_followers(id=user_id)[0])
except:
    followers = 0
try:
    followings = len(client.get_users_following(id=user_id)[0])
except:
    followings = 0
try:
    mentions = client.get_users_mentions(id=user_id)[0]
except:
    mentions = 0
try:
    tweets = len(client.get_users_tweets(id=user_id)[0])
except:
    tweets = 0
try:
    liked_tweet = len(client.get_liked_tweets(id=user_id)[0])
except:
    liked_tweet = 0
# get_tweet = client.get_tweet(id=1514564579946541060)
# print(get_tweet[0].text)

print('Followers :', followers)
print('Followings :', followings)
print('Mentioned in Messages :', mentions)
print('No. of Tweets :', tweets)
print('No. of Liked Tweets :',liked_tweet)

# quote = client.get_quote_tweets(id=1514564579946541060)


