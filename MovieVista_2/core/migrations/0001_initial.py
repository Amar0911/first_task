# Generated by Django 5.1.1 on 2024-11-12 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel_movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('CAROUSEL', 'carousel')], max_length=20)),
                ('movie_vista_original', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('release_year', models.IntegerField()),
                ('imdb', models.CharField(default='IMDB', max_length=20)),
                ('rating', models.IntegerField()),
                ('carousel_image', models.ImageField(upload_to='carousel_images')),
            ],
        ),
    ]