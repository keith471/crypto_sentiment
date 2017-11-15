from flask import Flask, Response
from mongoengine import connect
from argparse import ArgumentParser
from db.models import Coin, StockTwitsCursor, TextSummary, Price

from config.environment import Environment

import json
from datetime import datetime, timedelta
from decimal import Decimal

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

app = Flask(__name__)

# helper function for deserialization of decimal/datetime
def default(obj):
	if isinstance(obj, Decimal):
		return str(obj)
	elif isinstance(obj, datetime):
		return str(obj)
	raise TypeError("Object of type '%s' is not JSON serializable" % type(obj).__name__)

@app.route('/')
def home():
	return app.send_static_file('index.html')

@app.route('/<path:path>')
def static_proxy(path):
	return app.send_static_file(path)

@app.route('/api/coins')
def coins():
	json_arr = []
	for coin in Coin.objects:
		data = {}
		data['ticker'] = coin.ticker
		data['name'] = coin.name
		json_arr.append(data)
	return Response(json.dumps(json_arr, default=default), mimetype='application/json')

@app.route('/api/prices/<ticker>')
def prices(ticker):
	coin = Coin.objects.get(ticker=ticker)
	prices = Price.objects(coin=coin,created_at__gte=(datetime.now() - timedelta(days=7)))
	json_arr = []
	for price in prices:
		data = {}
		data['price'] = price.price
		data['created_at'] = price.created_at
		json_arr.append(data)
	return Response(json.dumps(json_arr, default=default), mimetype='application/json')

@app.route('/api/textSummaries/<ticker>')
def text_summaries(ticker):
	coin = Coin.objects.get(ticker=ticker)
	text_summaries = TextSummary.objects(coin=coin,posted_at__gte=(datetime.now() - timedelta(days=7)))
	json_arr = []
	for text_summary in text_summaries:
		data = {}
		data['sentiment'] = text_summary.sentiment
		data['posted_at'] = text_summary.posted_at
		json_arr.append(data)
	return Response(json.dumps(json_arr, default=default), mimetype='application/json')

if __name__ == '__main__':
    app.run()