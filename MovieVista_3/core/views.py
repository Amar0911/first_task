from django.shortcuts import render,redirect
from .forms import Registerform,AuthenticationForm,ChangePasswordForm,AdminProfileForm,UserProfileForm,CustomerForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
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



############################################################## seemore ####################################################



def seemore_trending(request):
    tm = Trending_movies.objects.all()
    return render(request,'core/seemore_trending.html',{'tm': tm})


def seemore_anime(request):
    am = Anime_movies.objects.all()
    return render(request,'core/seemore_anime.html',{'am': am})


def seemore_indian(request):
    im = Indian_movies.objects.all()
    return render(request,'core/seemore_indian.html',{'im': im})


def seemore_webseries(request):
    ws = Webseries.objects.all()
    return render(request,'core/seemore_webseries.html',{'ws': ws})



def seemore_hollywood(request):
    hm = Hollywood.objects.all()
    return render(request,'core/seemore_hollywood.html',{'hm':hm})



############################################################## cardplay ####################################################


def cardplay(request,id):
    tm = Trending_movies.objects.get(pk=id)
    return render(request,'core/cardplay.html',{'tm': tm}) 




############################################################## Register ####################################################



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
    


############################################################## Login ###############################################################



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
    


############################################################## Logout ###############################################################




def log_out(request):
    logout(request)
    return redirect('index')
    


############################################################## Profile ###############################################################


    
def profile(request):
    if request.user.is_authenticated:
        if request.method =='POST':
            if request.user.is_superuser == True:
                adm = AdminProfileForm(request.POST, instance = request.user)
            else:
                adm = UserProfileForm(request.POST, instance = request.user)
            if adm.is_valid():
                adm.save()
                messages.success(request,'Profile Updated Successfully!!')
        else:
            if request.user.is_superuser == True:
                adm = AdminProfileForm(instance = request.user)
            else:
                adm = UserProfileForm(instance = request.user)
        return render(request,'core/profile.html', {'name': request.user, 'adm': adm})


############################################################## Footer ###############################################################


def about(request):
    return render(request,'core/about.html')

def contact(request):
    return render(request,'core/contact.html')



############################################################## Change Password ############################################################



def changepassword(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            cp = ChangePasswordForm(request.user, request.POST)
            if cp.is_valid():
                cp.save()
                update_session_auth_hash(request, cp.user)
                messages.success(request,'Password Change Successfully')
                return redirect('profile')
        else:
            cp = ChangePasswordForm(request.user)
        return render(request,'core/changepassword.html',{'cp':cp})
    else:
        return redirect('login')
    


############################################################## Edit Profile ###############################################################


