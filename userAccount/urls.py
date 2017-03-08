from django.conf.urls import url
from . import views
from django.views.static import serve
from django.contrib.auth.decorators import login_required
from django.conf import settings

urlpatterns =[
	#url(r'^media/(?P<path>.*>$', login_required(serve), {'document_root': settings.MEDIA_ROOT}),
	url(r'^sign/$', views.SignForm.as_view(), name='signForm'),
	url(r'^login/$', views.LoginForm.as_view(), name='loginForm'),
	url(r'^logout/$', views.logout, name='logout'),
	url(r'^checkFlag/$', views.checkFlag, name='checkFlag'),
	url(r'^index/$', views.IndexForm.as_view(), name='indexForm'),
	url(r'^ranking/$', views.RankingForm.as_view(), name='rankingForm'),
	url(r'^start/$', views.Start.as_view(), name='start'),
	
]

