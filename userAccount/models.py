from django.db import models
from django.contrib.auth.models import AbstractUser


class Question(models.Model):
	title = models.TextField()
	score = models.IntegerField(default=0)
	text = models.TextField()
	file = models.FileField()
	flag = models.TextField()

	def check_question(self, flag, user):
		if flag == self.flag:
			user.question.add(self)

class MyUser(AbstractUser):
	question = models.ManyToManyField(Question)

          