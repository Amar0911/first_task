from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def spiderman(request):
    context = {'superhero': {'spidy': 'spiderman', 'bat': 'batman'}, 'villian': ['Joker', 'Venom', 'sandman'] }
    return render(request,'marvel/spiderman.html',context)