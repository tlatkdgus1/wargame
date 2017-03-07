from django.conf.urls import url
from . import views

urlpatterns =[
	url(r'^sign/$', views.SignForm.as_view(), name='signForm'),
	url(r'^login/$', views.LoginForm.as_view(), name='loginForm'),
	url(r'^logout/$', views.logout, name='logout'),
	url(r'^checkFlag/$', views.checkFlag, name='checkFlag'),
	url(r'^index/$', views.IndexForm.as_view(), name='indexForm'),
	url(r'^ranking/$', views.RankingForm.as_view(), name='rankingForm'),
	url(r'^start/$', views.Start.as_view(), name='start'),
	
]

