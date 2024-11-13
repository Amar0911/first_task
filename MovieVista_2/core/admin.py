from django.contrib import admin
from .models import Carousel_movies,Trending_movies

# Register your models here.

@admin.register(Carousel_movies)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ['id','name','movie_vista_original','genre','description','release_year','imdb','rating']



@admin.register(Trending_movies)
class TrendingAdmin(admin.ModelAdmin):
    list_display = ['id','name','movie_vista_original','genre','description','release_year','imdb','rating']