from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def first(request):
    return HttpResponse('This is my first view function')
def second(request):
    return HttpResponse('<marquee>This is my second view function</marquee>')
    
