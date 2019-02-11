from django.conf import settings
from django.db import models

class Post(models.Model):
	"""username = models.charField(max_length=200)
	password = models.charField(max_length=200)"""
	login = models.TextField()
	def __init__(self):
		return self.login

