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
    path('seemore/',views.seemore,name='seemore'),
]



#--------- THis is will add file to media folder -----------
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)