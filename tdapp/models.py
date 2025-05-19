from django.db import models
from django.contrib.auth.models import User

class TaskModel(models.Model):
	task = models.CharField(max_length=200)
	cr_dt = models.DateTimeField(auto_now_add=True)
	status = models.BooleanField(default=False)
	user = models.ForeignKey(User, on_delete=models.CASCADE);


	def __str__(self):
		return str(self.user)
