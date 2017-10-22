from django.db import models

# Create your models here.

class BlogInfo(models.Model):
    name= models.CharField(max_length=10)
    title= models.CharField(max_length=20)
    content=models.TextField(max_length=200)

    def __str__(self):
        return self.title