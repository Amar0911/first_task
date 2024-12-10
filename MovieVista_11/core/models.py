from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Movie(models.Model):


    CATEGORY_CHOICES = [
        ('CAROUSEL','Carousel'),
        ('TRENDING','Trending'),
        ('ANIME', 'Anime'),
        ('INDIAN', 'Indian'),
        ('WEBSERIES','Webseries'),
        ('HOLLYWOOD','Hollywood')
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    mov_vi_ori = models.CharField(max_length=100, default= 'Movie Vista Original')
    genre = models.CharField(max_length=100)
    description=models.TextField()
    re_year = models.IntegerField()
    imdb = models.CharField(max_length=20, default='IMDB')
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    starcast = models.CharField(max_length=200)
    director = models.CharField(max_length=100)
    movie_image =models.ImageField(upload_to='movie_images')  
    video = models.FileField(upload_to='movie_videos')

    def __str__(self):
        return str(self.name)
    



class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    films = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
    

###############################################################################################################

class Contact(models.Model):
    name = models.CharField(max_length=100, default='')
    email = models.EmailField()
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)