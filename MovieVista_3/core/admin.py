from django.contrib import admin
from .models import Carousel_movies,Trending_movies,Anime_movies,Indian_movies,Webseries,Hollywood

# Register your models here.

@admin.register(Carousel_movies)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ['id','name','movie_vista_original','genre','description','release_year','imdb','rating']



@admin.register(Trending_movies)
class TrendingAdmin(admin.ModelAdmin):
    list_display = ['id','name','movie_vista_original','genre','description','release_year','imdb','rating']


@admin.register(Anime_movies)
class AnimeAdmin(admin.ModelAdmin):
    list_display = ['id','name','movie_vista_original','genre','description','release_year','imdb','rating']



@admin.register(Indian_movies)
class IndianAdmin(admin.ModelAdmin):
    list_display = ['id','name','movie_vista_original','genre','description','release_year','imdb','rating']


@admin.register(Webseries)
class WebseriesAdmin(admin.ModelAdmin):
    list_display = ['id','name','movie_vista_original','genre','description','release_year','imdb','rating']



@admin.register(Hollywood)
class HollywoodAdmin(admin.ModelAdmin):
    list_display = ['id','name','movie_vista_original','genre','description','release_year','imdb','rating']