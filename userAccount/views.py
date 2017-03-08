from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.views.generic import View
from django.utils import timezone
from .models import MyUser
from .models import Question
from django.contrib.auth import authenticate, login, logout as _logout


class IndexForm(View):
	def get(self, request, *args, **kwargs):
		questions = Question.objects.order_by('score')
		solveQuestions = request.user.question.all()
		return render(request, 'userAccount/index.html', {'questions': questions, 'solveQuestions':solveQuestions})
	
	def post(self, request, *args, **kwargs):
		questions = Question.objects.order_by('score')
		solveQuestions = request.user.question.all()
		return render(request, 'userAccount/index.html', {'questions': questions, 'solveQuestions':solveQuestions})

class Start(TemplateView):
	template_name='userAccount/index.html'

class SignForm(View):
	def get(self, request, *args, **kwargs):
		response = render(request, 'userAccount/signForm.html')
		return response
	
	def post(self, request, *args, **kwargs):
		questions = Question.objects.order_by('score')
		user_id = request.POST['user_id']
		user_pw = request.POST['user_pw']
		user_email = request.POST['user_email']

		try:
			user_model = MyUser.objects.create(username = user_id, email = user_email)
			user_model.set_password(user_pw)
			user_model.save()
		except:
			error = "This is already a registered ID."
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
			error = "Invalid ID or PW."
			return render(request, 'userAccount/loginForm.html', {'error':error})

def logout(request):
	_logout(request)
	questions = Question.objects.order_by('score')
	return render(request, 'userAccount/index.html')

def checkFlag(request):
	input_flag = request.POST['flag']
	current_user = request.user
	question = Question.objects.get(flag=input_flag)
	questions = Question.objects.order_by('score')
	solveQuestions = current_user.question.all()

	answer = ''
	if question == None:
		answer = 'Wrong !!'
	elif question in solveQuestions:
		answer = 'You are already solve this Question !!'
	else:
		current_user.question.add(question)
		current_user.score = current_user.score + question.score
		current_user.solve = timezone.now()
		current_user.save()
		answer = 'Good !! You are solve this Question !!'

	return render(request, 'userAccount/index.html', {'questions': questions, 'solveQuestions':solveQuestions, 'answer':answer})

class RankingForm(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'userAccount/rankingForm.html', {'users': MyUser.objects.order_by('-score', 'solve')})

	def post(self, request, *args, **kwargs):
		return render(request, 'userAccount/rankingForm.html', {'users': MyUser.objects.order_by('-score', 'solve')})
