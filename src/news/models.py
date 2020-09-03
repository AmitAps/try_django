from django.db import models

# Create your models here.

class Article(models.Model):
    #id = models.IntegerField() #pk
    title = models.TextField()
    slug = models.SlugField(unique=True) #hello world --> hello-world
    content = models.TextField(null=True, blank=True)
#2.52
