from models.coin import Coin
from datetime import datetime, timedelta
from mongoengine import connect

connect(
	db='crypto',
	username='frances',
	password='thuglife',
	host='mongodb://127.0.0.1'
)

## Add bitcoin as a coin of interest
btn = "BTC"
btc_coin = Coin.objects(ticker=btn)
if btc_coin.count() == 0:
	print 'adding BTC'
	Coin(ticker=btn,name="Bitcoin",validation_method="Pow",hashing_algorithm="sha256").save()
