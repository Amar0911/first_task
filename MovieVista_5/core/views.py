from django.shortcuts import render,redirect,get_object_or_404
from .forms import Registerform,AuthenticationForm,ChangePasswordForm,AdminProfileForm,UserProfileForm,ContactForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from .models import Carousel_movies,Trending_movies,Anime_movies,Indian_movies,Webseries,Hollywood,Movies


#================ Forgot Password ======================

from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.http import HttpResponse

##########################################################################################################################################


# Create your views here.


def index(request):
    cm = Carousel_movies.objects.all()   #cm - Craousel movie
    tm = Trending_movies.objects.all()   #tm - Trending movie
    am = Anime_movies.objects.all()      #am - Anime
    im = Indian_movies.objects.all()     #im - Indian movie
    ws = Webseries.objects.all()         #ws - Webseries
    hm = Hollywood.objects.all()         #hm - Hollywood movie
    return render(request,'core/index.html',{'cm':cm,'tm':tm, 'am':am, 'im':im, 'ws': ws, 'hm': hm})



############################################################## seemore ##############################################################



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

def cardplay_carousel(request,id):
    cm = Carousel_movies.objects.get(pk=id)
    return render(request,'core/cardplay_carousel.html',{'cm': cm}) 


def cardplay(request,id):
    tm = Trending_movies.objects.get(pk=id)
    return render(request,'core/cardplay.html',{'tm': tm}) 

def cardplay_anime(request,id):
    am = Anime_movies.objects.get(pk=id)
    return render(request,'core/cardplay_anime.html',{'am': am}) 

def cardplay_indian(request,id):
    im = Indian_movies.objects.get(pk=id)
    return render(request,'core/cardplay_indian.html',{'im': im}) 

def cardplay_webseries(request,id):
    ws = Webseries.objects.get(pk=id)
    return render(request,'core/cardplay_webseries.html',{'ws': ws}) 

def cardplay_hollywood(request,id):
    hm = Hollywood.objects.get(pk=id)
    return render(request,'core/cardplay_hollywood.html',{'hm': hm}) 




############################################################## Register ####################################################



def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            rf = Registerform (request.POST)
            if rf.is_valid():
                rf.save()
                messages.success(request,'Registration Successfull !!')
                email = request.POST['email']
                user = User.objects.filter(email=email).first()
                if user:
                    send_mail(
                        'Registration Successfull',
                        f'Thank you for choosing us!!',
                        'cricketguru798@gmail',  # Use a verified email address
                        [email],
                        fail_silently=False,
                    )
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
    else:
        return redirect('login')


############################################################## About ###############################################################


def about(request):
    return render(request,'core/about.html')


############################################################## Contact ########################################################


def contact(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                # Check if the email in the form matches the logged-in user's email
                user_email = form.cleaned_data.get('email')
                if user_email != request.user.email:
                    messages.error(request, 'The email address does not match your registered email.')
                else:
                    # Save the form
                    form.save()

                    # Send a thank-you email to the user
                    subject = "Thank You for Contacting Us"
                    message = f"Dear {request.user.username},\n\nThank you for reaching out! We have received your message and will get back to you soon.\n\nBest regards,\nMovieVista Team"
                    from_email = 'cricketguru798@gmail.com'
                    recipient_list = [user_email]

                    try:
                        send_mail(subject, message, from_email, recipient_list)
                        messages.success(request, 'Your request has been sent successfully, and a confirmation email has been sent to you.')
                    except Exception as e:
                        messages.error(request, f"Message sent, but there was an error sending the confirmation email: {e}")

                    return redirect('contact')
            else:
                messages.error(request, 'There was an error sending your message. Please try again.')
        else:
            form = ContactForm()
        return render(request, 'core/contact.html', {'form': form})
    else:
        return redirect('login')



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
    



############################################################# Forget Password #########################################################
    

def forgotpassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        user = User.objects.filter(email=email).first()
        if user:
            token = default_token_generator.make_token(user)
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            reset_url = request.build_absolute_uri(f'/resetpassword/{uidb64}/{token}/')           
            send_mail(
                'Password Reset',
                f'Click the following link to reset your password: {reset_url}',
                'cricketguru798@gmail.com', 
                [email],
                fail_silently=False,
            )
            return redirect('passwordresetdone')
        else:
            messages.success(request,'Please enter valid email address')
    return render(request, 'core/forgotpassword.html')                                        
    

def resetpassword(request, uidb64, token):
    if request.method == 'POST':
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            try:
                uid = force_str(urlsafe_base64_decode(uidb64))
                user = User.objects.get(pk=uid)
                if default_token_generator.check_token(user, token):
                    user.set_password(password)
                    user.save()
                    return redirect('passwordresetdone')
                else:
                    return HttpResponse('Token is invalid', status=400)
            except (TypeError, ValueError, OverflowError, User.DoesNotExist):
                return HttpResponse('Invalid link', status=400)
        else:
            return HttpResponse('Passwords do not match', status=400)
    return render(request, 'core/resetpassword.html')

def password_reset_done(request):
    return render(request, 'core/password_reset_done.html')




######################################################## Add to Watchlist ##############################################################



def watchlistadd(request, id):
    if request.user.is_authenticated:
        movie = Trending_movies.objects.get(pk=id)
        user = request.user
        if Movies.objects.filter(user=user, films=movie).exists():
            messages.error(request, 'This movie is already added in your Watchlist')
        else:
            Movies(user=user, films=movie).save()
            messages.success(request,'Added to Watchlist')
        return redirect('seemore_trending')
    else:
        return redirect('login')


def watchlist(request):
    if request.user.is_authenticated:
        movie = Movies.objects.filter(user=request.user)
        anime_movie = Movies.objects.filter(user=request.user)
        return render(request, 'core/watchlist.html',{'movie':movie,'anime_movie':anime_movie})
    else:
        return redirect('login')


def watchlist_remove(request, id):
    if request.user.is_authenticated:
        movie = get_object_or_404(Trending_movies, pk=id)
        user = request.user
        watchlist = Movies.objects.filter(user=user, films=movie).first()
        if watchlist:
            watchlist.delete()
            messages.success(request, 'Removed from Watchlist')
        else:
            messages.error(request, 'This movie is not your watchlist')
        return redirect('watchlist')
    else:
        return redirect('login')