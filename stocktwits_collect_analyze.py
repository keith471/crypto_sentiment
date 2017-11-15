import requests
from argparse import ArgumentParser
import logging
import os
import schedule
from datetime import *
import time

from sentiment.sentiment_analyzer import SentimentAnalyzer
from sentiment.preprocessor import Preprocessor

from mongoengine import connect
from db.models import TextSummary, Coin
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

# make sure setup.py was run first
btc_coin = Coin.objects(ticker='BTC').first()
assert(btc_coin is not None)

preproc = Preprocessor()
analyzer = SentimentAnalyzer(preproc)

logger = logging.getLogger()

def collect_analyze():
    # and just get a dump of the latest 30 messages
    r = requests.get('https://api.stocktwits.com/api/2/streams/symbol/BTC.json')
    assert(r.status_code == 200)

    # get last 30 summaries in the db
    textSummaries = TextSummary.objects[:30]

    # dedupe summaries and save
    for msg in r.json()['messages']:
        posted_at = datetime.strptime(msg['created_at'], "%Y-%m-%dT%H:%M:%SZ")
        if contains_object_with_date(textSummaries, posted_at):
            logger.info('found duplicate summary with posted_at date: %s' % posted_at)
        else:
            TextSummary(
                coin=btc_coin,
                sentiment=analyzer.get_sentiment(msg['body']),
                raw_text=msg['body'],
                posted_at=posted_at,
            ).save()
            logger.info('saving summary with posted_at date: %s' % posted_at)

def contains_object_with_date(textSummaries, posted_at):
    for textSummary in textSummaries:
        if textSummary.posted_at == posted_at:
            return True
    return False

schedule.every(30).minutes.do(collect_analyze)
collect_analyze()

while 1:
    schedule.run_pending()
    time.sleep(1)
