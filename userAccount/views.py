from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.views.generic import View
from .models import MyUser
from django.contrib.auth import authenticate, login, logout as _logout

class SignForm(View):
	def get(self, request, *args, **kwargs):
		response = render(request, 'userAccount/signForm.html')
		return response
	
	def post(self, request, *args, **kwargs):
		user_id = request.POST['user_id']
		user_pw = request.POST['user_pw']
		user_email = request.POST['user_email']

		user_model = MyUser.objects.create(username = user_id, email = user_email)
		user_model.set_password(user_pw)
		user_model.save()
		return render(request, 'userAccount/index.html')

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
			return render(request, 'userAccount/index.html')
		else:
			return render(request, 'userAccount/loginForm.html')

def logout(request):
	_logout(request)
	return render(request, 'userAccount/index.html')