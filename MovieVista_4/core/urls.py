from django.urls import path
from . import views


#------ To incude Media file ---------------
from django.conf import settings
from django.conf.urls.static import static
#------------------------------------------


urlpatterns = [
    path('',views.index,name='index'),
    path('signup/',views.register,name='signup'),
    path('profile/',views.profile,name='profile'),
    path('login/',views.log_in,name='login'),
    path('logout/',views.log_out,name='logout'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('changepassword/',views.changepassword,name='changepassword'),
    path('forgotpassword/',views.forgotpassword, name="forgotpassword"),
    path('resetpassword/<uidb64>/<token>/', views.resetpassword, name='resetpassword'),
    path('password_reset_done/', views.password_reset_done, name='passwordresetdone'),
    path('seemore_trending/',views.seemore_trending,name='seemore_trending'),
    path('seemore_anime/',views.seemore_anime,name='seemore_anime'),
    path('seemore_indian/',views.seemore_indian,name='seemore_indian'),
    path('seemore_webseries/',views.seemore_webseries,name='seemore_webseries'),
    path('seemore_hollywood/',views.seemore_hollywood,name='seemore_hollywood'),
    path('cardplay/<int:id>/',views.cardplay,name='cardplay'),
    path('cardplay_anime/<int:id>/',views.cardplay_anime,name='cardplay_anime'),
    path('cardplay_indian/<int:id>/',views.cardplay_indian,name='cardplay_indian'),
    path('cardplay_webseries/<int:id>/',views.cardplay_webseries,name='cardplay_webseries'),
    path('cardplay_hollywood/<int:id>/',views.cardplay_hollywood,name='cardplay_hollywood'),
    path('cardplay_carousel/<int:id>/',views.cardplay_carousel,name='cardplay_carousel'),
    path('watchlistadd/<int:id>/',views.watchlistadd,name='watchlistadd'),
    path('watchlist/',views.watchlist,name='watchlist'),
   

    
]



#--------- THis is will add file to media folder -----------
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)