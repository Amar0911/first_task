from django.urls import path
from . import views



urlpatterns = [
    path('',views.index,name='index'),
    path('signup/',views.register,name='signup'),
    path('profile/',views.profile,name='profile'),
    path('login/',views.log_in,name='login'),
    path('logout/',views.log_out,name='logout'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
]

