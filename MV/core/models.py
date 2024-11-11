from django.db import models

# Create your models here.

class Trending(models.Model):

    CATEGORY_CHOICES = [
        ('CAROUSEL', 'carousel'),
        ('TRENDING', 'trending'),
        ('ANIME', 'anime'),
        ('WEBSERIES', 'webseries'),
        ('INDIAN_MOVIES', 'indian_movies'),
        ('HOLLYWOOD_MOVIES', 'hollywood_movies'), 
    ]


    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Trending')
    release_date = models.DateField()
    movie_duration = models.TimeField()
    description=models.TextField()
    movie_image =models.ImageField(upload_to='movie_images')  

    def __str__(self):
        return str(self.name)