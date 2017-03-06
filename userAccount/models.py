from django.db import models
from django.contrib.auth.models import AbstractUser


class Question(models.Model):
	title = models.TextField()
	score = models.IntegerField(default=0)
	text = models.TextField()
	file = models.FileField('question/', blank=True, null=True)
	flag = models.TextField(unique=True)


class MyUser(AbstractUser):
	question = models.ManyToManyField(Question)

          