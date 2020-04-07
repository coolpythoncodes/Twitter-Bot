import tweepy
import config
import time

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True)

file_name = 'last_seen.txt'

# Make a tweet
# api.update_status('Happy Sunday')

def read_last_seen(file_name):
    file_read = open(file_name,'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(file_name, last_seen_id):
    file_write = open(file_name,'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

def reply():
    # Get tweet that I was mentioned
    tweets = api.mentions_timeline(read_last_seen(file_name), tweet_mode = 'extended')
    for tweet in reversed(tweets):
        if '@classicdude1' in tweet.full_text.lower():
            print(tweet.full_text)
            api.update_status(f"@{tweet.user.screen_name} Thanks for keeping us posted with relevant news", tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            store_last_seen(file_name,tweet.id)

while True:
    reply()
    time.sleep(30)

# # Get text in a tweet
# print(tweets[0].full_text)

# for tweet in tweets:
#     print(f'{tweet.id} - {tweet.full_text}')





# # To check if a particular keyword or hashtag is in a mention tweet of you
# for tweet in tweets:
#     if '#pastorosagieizeiyamu' in tweet.full_text.lower():
#         print(f'{tweet.id} - {tweet.full_text}')

