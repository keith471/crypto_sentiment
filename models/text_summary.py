'''an object that records processed information related to a post or text document about cryptocurrency'''
from mongoengine import Document
from mongoengine.fields import *
from coin import Coin
from datetime import *

class TextSummary(Document):
	coin = ReferenceField(Coin)
	raw_text = StringField(max_length=130)
	sentiment = IntField()
	tags = ListField(StringField(max_length=10)) 
	user_id = UUIDField()
	reshare_count = IntField()
	reshare_users = ListField(UUIDField()) 
	posted_at = DateTimeField()
	created_at = DateTimeField(default=datetime.utcnow)
	updated_at = DateTimeField(default=datetime.utcnow)
	meta = {
		'allow_inheritance': True,
		'ordering': ['-posted_at'],
		'indexes': [
			'coin',
			'tags',
			'user_id',
			'posted_at',
			'created_at',
			'updated_at'
		]
	}
	