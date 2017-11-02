'''an object that encapsulates information about a text provider'''
from mongoengine import Document
from mongoengine.fields import *
from datetime import *

class Provider(Document):
	name = StringField(max_length=128)
	weight = IntField()
	meta = {
		'allow_inheritance': True,
		'ordering': ['name'],
		'indexes': [
			'name',
			'weight'
		]
	}
