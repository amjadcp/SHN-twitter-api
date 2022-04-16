import tweepy
from keys import *


# client = tweepy.Client(bearer_token)

# user = client.get_user(username='Naheel360')
# user_id = user[0].id
# print(client.get_users_followers(id=user_id))


client = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,
)

user = client.get_user(username='Naheel360')
user_id = user[0].id
# print(client.get_users_followers(id=user_id))

# mentions = client.get_users_mentions(id=user_id)
# for mention in mentions[0]:
#     print(mention)

# details of me
# me = client.get_me()
# print(me[0].id)

#tweets of that user
# tweets = client.get_users_tweets(id=user_id)
# print(tweets)

auth = tweepy.OAuth2BearerHandler(bearer_token)
api = tweepy.API(auth)
api.retweet(id=1488439159299526657)
