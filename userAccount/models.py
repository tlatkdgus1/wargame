from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.conf import settings 

class Question(models.Model):
	title = models.TextField()
	score = models.IntegerField(default=0)
	text = models.TextField()
	url = models.URLField(blank=True, null=True)
	file = models.FileField(blank=True, null=True)
	flag = models.TextField(unique=True)


class MyUser(AbstractUser):
	question = models.ManyToManyField(Question)
	score = models.IntegerField(default=0)
	solve = models.DateTimeField(default=timezone.now)

          