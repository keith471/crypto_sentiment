'''
	An object that will allow us to track where we left off in the collection of tweets. 
	We could save one after every collection to track the range of data collected.
'''
from mongoengine import Document
from mongoengine.fields import *
from datetime import *

class StockTwitsCursor(Document):
	more = BooleanField()
	since = UUIDField()
	maximum = UUIDField()
	created_at = DateTimeField(default=datetime.utcnow)
	meta = {
		'allow_inheritance': True,
		'ordering': ['-created_at'],
		'indexes': [
			'created_at'
		]
	}