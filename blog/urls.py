'''
Date: 2021-03-30 19:35:05
'''
from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('<int:page_id>', views.blog, name='blog'),
]
