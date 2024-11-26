from django.contrib import admin
from .models import Carousel_movies,Trending_movies,Anime_movies,Indian_movies,Webseries,Hollywood,CustomerDetail,Movies

# Register your models here.

@admin.register(Carousel_movies)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ['id','name','movie_vista_original','genre','description','release_year','imdb','rating','starcast','director']



@admin.register(Trending_movies)
class TrendingAdmin(admin.ModelAdmin):
    list_display = ['id','name','movie_vista_original','genre','description','release_year','imdb','rating','starcast','director']


@admin.register(Anime_movies)
class AnimeAdmin(admin.ModelAdmin):
    list_display = ['id','name','movie_vista_original','genre','description','release_year','imdb','rating','starcast','director']



@admin.register(Indian_movies)
class IndianAdmin(admin.ModelAdmin):
    list_display = ['id','name','movie_vista_original','genre','description','release_year','imdb','rating','starcast','director']


@admin.register(Webseries)
class WebseriesAdmin(admin.ModelAdmin):
    list_display = ['id','name','movie_vista_original','genre','description','release_year','imdb','rating','starcast','director']



@admin.register(Hollywood)
class HollywoodAdmin(admin.ModelAdmin):
    list_display = ['id','name','movie_vista_original','genre','description','release_year','imdb','rating','starcast','director']



@admin.register(CustomerDetail)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','address','city','state','pincode']


@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'films']