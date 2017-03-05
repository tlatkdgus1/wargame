from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
	question = models.ManytoMany(Question)

class Question(models.Model):
	title = models.TextField(maxlength=20)
	score = models.IntegerField(default=0)
	text = models.TextField(maxlength=300)
	file = models.fileField(maxlength=20)
	flag = models.TextField(maxlength=50)


	def check_question(self, flag, user):
    	if flag == self.flag:
        	user.question.add(self)
          