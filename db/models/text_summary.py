'''an object that records processed information related to a post or text document about cryptocurrency'''
from mongoengine import Document
from mongoengine.fields import *
from .provider import Provider
from .coin import Coin
from datetime import *

class TextSummary(Document):
	provider = ReferenceField(Provider)
	coin = ReferenceField(Coin)
	raw_text = StringField(max_length=512)
	sentiment = DecimalField()
	score = DecimalField()
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
			'provider',
			'coin',
			'tags',
			'user_id',
			'posted_at',
			'created_at',
			'updated_at'
		]
	}
