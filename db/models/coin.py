'''An object to represent a cryptocurrency in the system'''
from mongoengine import Document
from mongoengine.fields import *

class Coin(Document):
	ticker = StringField(max_length=5)
	name = StringField(max_length=20)
	validation_method = StringField(max_length=10)
	hashing_algorithm = StringField(max_length=10)
	meta = {
		'allow_inheritance': True,
		'indexes': [
			'ticker',
			'validation_method', 
			'hashing_algorithm' 
		]
	}
