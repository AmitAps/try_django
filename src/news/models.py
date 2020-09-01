from django.db import models

# Create your models here.

class Article(models.Model):
    #id = models.IntegerField()
    title = models.TextField()
    content = models.TextField(null=True, blank=True)
#1.36
