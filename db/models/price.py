'''an object that records the price of a cryptocurrency in USD'''
from mongoengine import Document
from mongoengine.fields import *
from .coin import Coin
from datetime import *

class Price(Document):
	coin = ReferenceField(Coin)
	price = DecimalField()
	created_at = DateTimeField(default=datetime.utcnow)
	meta = {
		'allow_inheritance': True,
		'ordering': ['-created_at'],
		'indexes': [
			'coin',
			'created_at'
		]
	}
