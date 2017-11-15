import requests
from mongoengine import connect
from db.models import Coin, Price

from datetime import *
import time
import schedule
import logging

from config.environment import Environment
from argparse import ArgumentParser

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

logger = logging.getLogger()

btc_coin = Coin.objects(ticker='BTC').first()
assert(btc_coin is not None)

def collect():
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD')
    assert(r.status_code == 200)
    msg = r.json()
    now = datetime.now()
    Price(
        coin=btc_coin,
        price=msg['USD'],
        created_at=now
    ).save()
    logger.info('saving coin price at date: %s' % now)

schedule.every(10).minutes.do(collect)
collect()

while 1:
    schedule.run_pending()
    time.sleep(1)
