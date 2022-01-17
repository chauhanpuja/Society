from django.db import models

# Create your models here.
class Post(models.Model):
    slug=models.SlugField(max_length=100)
    title=models.CharField(max_length=200)
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='image')
    
    desc=models.TextField()
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Shop(models.Model):
    slug=models.SlugField(max_length=100)
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='image')
    price=models.IntegerField()
    desc=models.TextField()
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
