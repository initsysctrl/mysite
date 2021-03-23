'''
Date: 2021-03-23 10:20:15
'''
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("hello ,you are in a polls index")
