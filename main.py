import tweepy

client = tweepy.Client("BEARER TOKEN HERE")



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

print('Followers :', followers)
print('Followings :', followings)
print('Mentioned in Messages :', mentions)
print('No. of Tweets :', tweets)
print('No. of Liked Tweets :',liked_tweet)


