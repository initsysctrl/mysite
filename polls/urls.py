'''
Date: 2021-03-23 10:22:53
'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')
]
