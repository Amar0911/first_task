from django.db import models
from django.contrib.auth.models import User

# Create your models here.



############################################################## Categories ####################################################



class Carousel_movies(models.Model):
      

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20)
    movie_vista_original = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description=models.TextField()
    release_year = models.IntegerField()
    imdb = models.CharField(max_length=20, default='IMDB')
    rating = models.DecimalField(max_digits=3, decimal_places=1, default='0.0')
    starcast = models.CharField(max_length=200, default=2)
    director = models.CharField(max_length=100, default=2)
    carousel_image =models.ImageField(upload_to='carousel_images')  

    def __str__(self):
        return str(self.name)
    

class Trending_movies(models.Model):
    

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20)
    movie_vista_original = models.CharField(max_length=100, default= 'Movie Vista Original')
    genre = models.CharField(max_length=100)
    description=models.TextField()
    release_year = models.IntegerField()
    imdb = models.CharField(max_length=20, default='IMDB')
    rating = models.DecimalField(max_digits=3, decimal_places=1, default='0.0')
    starcast = models.CharField(max_length=200, default=2)
    director = models.CharField(max_length=100, default=2)
    trending_image =models.ImageField(upload_to='trending_images')  

    def __str__(self):
        return str(self.name)
    




class Anime_movies(models.Model):
    

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20)
    movie_vista_original = models.CharField(max_length=100, default= 'Movie Vista Original')
    genre = models.CharField(max_length=100)
    description=models.TextField()
    release_year = models.IntegerField()
    imdb = models.CharField(max_length=20, default='IMDB')
    rating = models.DecimalField(max_digits=3, decimal_places=1, default='0.0')
    starcast = models.CharField(max_length=200, default=2)
    director = models.CharField(max_length=100, default=2)
    anime_image =models.ImageField(upload_to='anime_images')  

    def __str__(self):
        return str(self.name)
    


class Indian_movies(models.Model):
    

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20)
    movie_vista_original = models.CharField(max_length=100, default= 'Movie Vista Original')
    genre = models.CharField(max_length=100)
    description=models.TextField()
    release_year = models.IntegerField()
    imdb = models.CharField(max_length=20, default='IMDB')
    rating = models.DecimalField(max_digits=3, decimal_places=1, default='0.0')
    starcast = models.CharField(max_length=200, default=2)
    director = models.CharField(max_length=100, default=2)
    indian_image =models.ImageField(upload_to='indian_images')  

    def __str__(self):
        return str(self.name)
    


class Webseries(models.Model):

    name = models.CharField(max_length=100)
    movie_vista_original = models.CharField(max_length=100, default= 'Movie Vista Original')
    genre = models.CharField(max_length=100)
    description=models.TextField()
    release_year = models.IntegerField()
    imdb = models.CharField(max_length=20, default='IMDB')
    rating = models.DecimalField(max_digits=3, decimal_places=1, default='0.0')
    starcast = models.CharField(max_length=200, default=2)
    director = models.CharField(max_length=100, default=2)
    webseries_image =models.ImageField(upload_to='webseries_images')  

    def __str__(self):
        return str(self.name)
    


class Hollywood(models.Model):

    name = models.CharField(max_length=100)
    movie_vista_original = models.CharField(max_length=100, default= 'Movie Vista Original')
    genre = models.CharField(max_length=100)
    description=models.TextField()
    release_year = models.IntegerField()
    imdb = models.CharField(max_length=20, default='IMDB')
    rating = models.DecimalField(max_digits=3, decimal_places=1, default='0.0')
    starcast = models.CharField(max_length=200, default=2)
    director = models.CharField(max_length=100, default=2)
    hollywood_image =models.ImageField(upload_to='hollywood_images')  

    def __str__(self):
        return str(self.name)
    

#############################################################################################################################

class Movies(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    films = models.ForeignKey(Trending_movies, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) 


#############################################################################################################################

class Contact(models.Model):
    name = models.CharField(max_length=100, default='')
    email = models.EmailField()
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)