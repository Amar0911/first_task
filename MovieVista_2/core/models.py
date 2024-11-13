from django.db import models

# Create your models here.


class Carousel_movies(models.Model):
    
    
    CATEGORY_CHOICES = [
        ('CAROUSEL' , 'carousel')
    ]


    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    movie_vista_original = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description=models.TextField()
    release_year = models.IntegerField()
    imdb = models.CharField(max_length=20, default='IMDB')
    rating = models.DecimalField(max_digits=3, decimal_places=1, default='0.0')
    carousel_image =models.ImageField(upload_to='carousel_images')  

    def __str__(self):
        return str(self.name)
    

class Trending_movies(models.Model):


    
    TRENDING_CHOICES = [
        ('TRENDING' , 'trending')
    ]


    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=TRENDING_CHOICES)
    movie_vista_original = models.CharField(max_length=100, default= 'Movie Vista Original')
    genre = models.CharField(max_length=100)
    description=models.TextField()
    release_year = models.IntegerField()
    imdb = models.CharField(max_length=20, default='IMDB')
    rating = models.DecimalField(max_digits=3, decimal_places=1, default='0.0')
    trending_image =models.ImageField(upload_to='trending_images')  

    def __str__(self):
        return str(self.name)