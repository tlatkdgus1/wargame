from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.views.generic import View
from .models import MyUser
from .models import Question
from django.contrib.auth import authenticate, login, logout as _logout


class SignForm(View):
	def get(self, request, *args, **kwargs):
		response = render(request, 'userAccount/signForm.html')
		return response
	
	def post(self, request, *args, **kwargs):

		questions = Question.objects.order_by('score')

		user_id = request.POST['user_id']
		user_pw = request.POST['user_pw']
		user_email = request.POST['user_email']

		if MyUser.objects.get(username=user_id) is None:
			user_model = MyUser.objects.create(username = user_id, email = user_email)
			user_model.set_password(user_pw)
			user_model.save()
		else:
			error = "Already Register ID"
			return render(request, 'userAccount/signForm.html', {'error':error})

		return render(request, 'userAccount/index.html', {'questions': questions})

class LoginForm(View):
	def get(self, request, *args, **kwargs):
		response = render(request, 'userAccount/loginForm.html')
		return response

	def post(self, request, *args, **kwargs):
		user_id = request.POST['user_id']
		user_pw = request.POST['user_pw']
		user = authenticate(username=user_id, password=user_pw)
		if user is not None:
			login(request, user)
			questions = Question.objects.order_by('score')
			solveQuestions = user.question.all()
			return render(request, 'userAccount/index.html', {'questions': questions, 'solveQuestions':solveQuestions})
		else:	
			error = "ID or PW is Wrong"
			return render(request, 'userAccount/loginForm.html', {'error':error})

def logout(request):
	_logout(request)
	questions = Question.objects.order_by('score')
	return render(request, 'userAccount/index.html', {'questions': questions})

def checkFlag(request):
	input_flag = request.POST['flag']
	current_user = request.user
	question = Question.objects.get(flag=input_flag)
	questions = Question.objects.order_by('score')
	solveQuestions = current_user.question.all()

	if question is None:
		answer = 'Wrong !!'
	elif question in solveQuestions:
		answer = 'You are already solve this Question !!'
	else:
		current_user.question.add(question)
		current_user.score = current_user.score + question.score
		current_user.save()
		answer = 'Good !! You are solve this Question !!'

	return render(request, 'userAccount/index.html', {'questions': questions, 'solveQuestions':solveQuestions})