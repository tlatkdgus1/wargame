from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^user/', include('userAccount.urls', namespace='user')),
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}),
]
