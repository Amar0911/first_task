from django.shortcuts import render
from .forms import MarvelForm
# Create your views here.

def index(request):
    MF = MarvelForm()
    return render(request,'core/index.html',{'MarvelForm':MF})