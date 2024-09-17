from django.urls import path
from . import views

urlpatterns = [
    path('batman/', views.batman),
    path('superman/', views.superman),
    path('flash/', views.flash),

]