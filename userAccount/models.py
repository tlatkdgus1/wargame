from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
	question = models.ManytoMany(Question)

class Question(models.Model):
	title = models.TextField(maxlength=20)
	score = models.IntegerField(default=0)
	text = models.TextField(maxlength=300)
	file = models.fileField(maxlength=20)
	answer = models.TextField(maxlength=50)