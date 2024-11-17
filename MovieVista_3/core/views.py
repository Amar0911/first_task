from django.shortcuts import render,redirect
from .forms import Registerform,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Carousel_movies,Trending_movies,Anime_movies,Indian_movies,Webseries,Hollywood

# Create your views here.

def index(request):
    cm = Carousel_movies.objects.all()   #cm - Craousel movie
    tm = Trending_movies.objects.all()   #tm - Trending movie
    am = Anime_movies.objects.all()      #am - Anime
    im = Indian_movies.objects.all()     #im - Indian movie
    ws = Webseries.objects.all()         #ws - Webseries
    hm = Hollywood.objects.all()         #hm - Hollywood movie
    return render(request,'core/index.html',{'cm':cm,'tm':tm, 'am':am, 'im':im, 'ws': ws, 'hm': hm})



def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            rf = Registerform (request.POST)
            if rf.is_valid():
                rf.save()
                return redirect('login')
        else:
            rf = Registerform()
        return render(request,'core/signup.html',{'rf':rf})
    else:
        return redirect('profile')
    

def log_in(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            rf = AuthenticationForm(request,request.POST)
            if rf.is_valid():
                name = rf.cleaned_data['username']
                pas = rf.cleaned_data['password']
                user = authenticate(username=name, password=pas)
                if user is not None:
                    login(request, user)
                    return redirect('/')
                else:
                    messages.error(request,'Invalid username and password')
        else:
            rf = AuthenticationForm()
        return render(request,'core/login.html',{'rf':rf})   
    else:
        return redirect('profile') 
    


def log_out(request):
    logout(request)
    return redirect('index')
    

    
def profile(request):
    return render(request,'core/profile.html')


def about(request):
    return render(request,'core/about.html')

def contact(request):
    return render(request,'core/contact.html')

