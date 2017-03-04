from django.conf.urls import url
from . import views

urlpatterns =[
	url(r'^sign/$', views.signForm.as_view(), name='signForm'),
	url(r'^login/$', views.loginForm.as_view(), name='loginForm'),
	url(r'^logout/$', views.logout, name='logout'),
]
