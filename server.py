from flask import Flask
from mongoengine import connect

from models.coin import Coin
from models.stock_twits_cursor import StockTwitsCursor
from models.text_summary import TextSummary
from models.price import Price

import json
from datetime import datetime, timedelta
from decimal import Decimal

connect(
	db='crypto',
	username='frances',
	password='thuglife',
	host='mongodb://127.0.0.1'
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
	Coin.objects
	json_arr = []
	for coin in Coin.objects:
		data = {}
		data['ticker'] = coin.ticker
		data['name'] = coin.name
		json_arr.append(data)
	return json.dumps(json_arr, default=default)

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
	return json.dumps(json_arr, default=default)

@app.route('/api/textSummaries/<ticker>')
def text_summaries(ticker):
	coin = Coin.objects.get(ticker=ticker)
	text_summaries = TextSummary.objects(coin=coin,created_at__gte=(datetime.now() - timedelta(days=7)))
	json_arr = []
	for text_summary in text_summaries:
		data = {}
		data['sentiment'] = text_summary.sentiment
		data['created_at'] = text_summary.created_at
		json_arr.append(data)
	return json.dumps(json_arr, default=default)
