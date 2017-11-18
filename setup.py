from db.models import Coin
from datetime import datetime, timedelta
from mongoengine import connect
from argparse import ArgumentParser
from config.environment import Environment

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

## Add bitcoin as a coin of interest
btn = "BTC"
btc_coin = Coin.objects(ticker=btn)
if btc_coin.count() == 0:
	print('adding BTC')
	Coin(ticker=btn,name="Bitcoin",validation_method="Pow",hashing_algorithm="sha256").save()

eth = "ETH"
eth_coin = Coin.objects(ticker=eth)
if eth_coin.count() == 0:
	print('adding ETH')
	Coin(ticker=eth,name="Ethereum",validation_method="PoS",hashing_algorithm="ethash").save()

# TODO: initialize stock_twits_cursor
