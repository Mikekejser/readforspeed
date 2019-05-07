from django.db import models
from django.contrib.auth.models import User


class Text(models.Model):
	text = models.TextField()
	
	def __str__(self):
		return self.text


class UserText(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=40)
	text = models.CharField(max_length=10000)

	def __str__(self):
		return f'{self.user.username} | {self.title}'



# class UserSettings(models.Model):
# 	user = models.OneToOneField(User, on_delete=models.CASCADE)
