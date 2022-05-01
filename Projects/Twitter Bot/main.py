import tweepy
import time

auth = tweepy.OAuth1UserHandler(
# API key
   'qP63wtYDbRGuE6KASxXFZdbAa',
# API key secret
   'v3iRdtSSsxqHxaOlGZIRdTlLJmZshGGCI65webc6dqmeMoc6hV',
# Access token
   '1246451238-7RtHsFcjrrXCoVlXuaDxb4tdoYMeSCit1CIVEAv',
# Access token secret
   '4VIzCm24Rrzm3HAeJWLnUUdHKQv84L2XJMEJC7UUOIMHh'
)

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)

api = tweepy.API(auth)

# Code to follow a user and to get the details of a user
# user = api.get_user(screen_name='AndreiNeagoie')
# user.follow()

# get the list of followers
# for follower in api.get_followers():
#     if follower.screen_name == 'niravpatel2890':
#        follower.follow()


# user = api.get_user(screen_name='AndreiNeagoie')
# print(user.followers_count)

# print public tweets
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)


