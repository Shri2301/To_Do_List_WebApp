from django.db import models
from django.contrib.auth.models import User

class OtpModel(models.Model):
	otp = models.IntegerField(primary_key=True)
	username = models.TextField(max_length=60)
	email = models.EmailField()
	password = models.TextField()


	def __str__(self):
		return str(self.username)
