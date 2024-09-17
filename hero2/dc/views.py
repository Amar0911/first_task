from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def batman(request):
    return HttpResponse('I am a batman')

def superman(request):
    return HttpResponse('I am a superman')

def flash(request):
    return HttpResponse('I am a flash')