import oauth2 as oauth

from argparse import ArgumentParser
import logging
import time
import json

from config.environment import Environment

#===============================================================================
# Arugment parsing
#===============================================================================

parser = ArgumentParser()
parser.add_argument('env', type=str, action='store', help='the environment')
parser.add_argument('--h', action='store_true', help='if set, usage will be printed out')
args = parser.parse_args()

if args.h:
    parser.print_help()

env = Environment(args.env)


consumer = oauth.Consumer(key=env.APP_KEY, secret=env.APP_SECRET)
token = oauth.Token(key=env.TOKEN, secret=env.TOKEN_SECRET)
client = oauth.Client(consumer, token)

endpoint = "https://api.twitter.com/1.1/search/tweets.json?q=$BTC"
response, data = client.request(endpoint)
tweets = json.loads(data)
