from django.db import models

# Create your models here.

class Review(models.Model):
    title=models.CharField(max_length=50)
    release_year=models.IntegerField()
    genre=models.CharField(max_length=20)
    star_rating=models.FloatField()
    running_time=models.IntegerField() #분단위
    content=models.TextField()
    director=models.CharField(max_length=20)
    actors=models.CharField(max_length=50)
    
    
    
    