from django.conf import settings
from django.db import models

# Create your models here.

User = settings.AUTH_USER_MODEL

class Article(models.Model):
    #id = models.IntegerField() #pk
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=240)
    slug = models.SlugField(unique=True) #hello world --> hello-world
    content = models.TextField(null=True, blank=True)

    def get_absolute_url(self):
        return f"/news/{ self.id}/{self.slug}"

    def get_edit_url(self):
        return f"{ self.get_absolute_url()}/edit/"

    def get_delete_url(self):
        return f"{ self.get_absolute_url() }/delete/"
#3.28
#42
