'''
Date: 2021-03-23 10:20:15
'''
from django.contrib import admin
from .models import Question, Blog
# Register your models here.
admin.site.register(Question)
admin.site.register(Blog)
