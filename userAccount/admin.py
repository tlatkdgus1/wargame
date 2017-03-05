from django.contrib import admin
from .models import MyUser
from .models import Question

admin.site.register(MyUser)
admin.site.register(Question)
