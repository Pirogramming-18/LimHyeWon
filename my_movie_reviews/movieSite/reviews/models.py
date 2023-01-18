from django.db import models

# Create your models here.

class Review(models.Model):
    GENRE_CHOCIES=(
        ('SF','SF'),('DRAMA','DRAMA'),('ROMANCE','ROMANCE'),('HISTORY','HISTORY'),('MUSICAL','MUSICAL'),('ANIMATION','ANIMATION'),('HORROR','HORROR'))
    title=models.CharField(max_length=50)
    release_year=models.IntegerField()
    genre=models.CharField(max_length=20,choices=GENRE_CHOCIES)
    star_rating=models.FloatField()
    running_time=models.IntegerField() #분단위
    content=models.TextField()
    director=models.CharField(max_length=20)
    actors=models.CharField(max_length=80)
    
    
    
    