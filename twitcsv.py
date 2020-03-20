import tweepy
import csv
import pandas as pd
####input your credentials here
consumer_key = 'y8Fmd5yY0Z9ZXkGFlzMfirfah'
consumer_secret = '2ryyN1QpuaAUuIpkk2zPyevoRcErLkENX61vSzxo15rOXmQeeS'
access_token = '1933344672-3j6muKL8kqly35xk8CAYfJmoHcw4LC3jbOQ6iod'
access_token_secret = 'aVzGGPe9J33LdGe8jbbC8hC07ovijLvrduyboBnR5sSMs'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('result.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#corona",count=10,
                           lang="en",
                           since="2020-03-03").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])