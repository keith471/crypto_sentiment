'''Example using new preprocessing technique'''
from __future__ import print_function

from argparse import ArgumentParser
import sys
import os

from sentiment.sentiment_analyzer import SentimentAnalyzer
from sentiment.preprocessor import Preprocessor

from mongoengine import connect

from db.models import TextSummary
from environment import Environment

#===============================================================================
# Arugment parsing
#===============================================================================

parser = ArgumentParser()
parser.add_argument('env', type=str, action='store', help='the environment')
parser.add_argument('--h', action='store_true', help='if set, usage will be printed out')
args = parser.parse_args()

## TODO error checking on the args

if args.h:
    parser.print_help()

print()

#===============================================================================
# Connecting to MongoDB
#===============================================================================

env = Environment(args.env)
connect(
    db=env.DB_NAME,
    username=env.DB_USERNAME,
    password=env.DB_PASSWORD,
    host='mongodb://' + env.DB_HOST
)

#===============================================================================
# Main
#===============================================================================

if __name__ == '__main__':
    preproc = Preprocessor()
    analyzer = SentimentAnalyzer(preproc)

    # get sentiment for all text_summary objects in the db
    for text_summary in TextSummary.objects:
        sentiment = analyzer.get_sentiment(text_summary.raw_text)
        print('Sentiment: %f' % sentiment)
        # text_summary.sentiment = sentiment;
        # text_summary.save()
        print()
