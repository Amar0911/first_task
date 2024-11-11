from django.shortcuts import render,redirect
from .models import Trending

# Create your views here.

def index(request):
    trend=Trending.objects.all()
    return render(request,'core/index.html',{'trend':trend})


