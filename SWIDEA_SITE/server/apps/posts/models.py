from django.db import models

# Create your models here.

class Devtool(models.Model):
    name=models.CharField(max_length=10)
    kind=models.CharField(max_length=30)
    content=models.TextField()

class Idea(models.Model):

    title=models.CharField(max_length=20)
    image=models.ImageField(blank=True,upload_to='posts/%Y%m%d')
    content=models.TextField()
    interest=models.IntegerField()
    
    tool=models.ForeignKey(Devtool,on_delete=models.CASCADE,related_name="used_tool")
    
    
    
    
    
