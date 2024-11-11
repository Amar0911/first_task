from django.contrib import admin
from .models import Trending
# Register your models here.


@admin.register(Trending)
class TrendingAdmin(admin.ModelAdmin):
    list_display = ['id','name','category','release_date','movie_duration','description']