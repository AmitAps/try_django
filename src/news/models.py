from django.conf import settings
from django.db import models
from django.db.models import Q
from django.utils import timezone
# Create your models here.

User = settings.AUTH_USER_MODEL

class ArticleQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.filter(publish_date__lte=now)

    def search(self, query):
        lookup = (Q(title__icontains=query)
                | Q(content__icontains=query)
                | Q(slug__icontains=query)
                | Q(user__first_name__icontains=query)
                | Q(user__last_name__icontains=query)
                | Q(user__username__icontains=query))
        return self.filter(lookup)

class ArtileManager(models.Manager):
    def get_queryset(self):
        return ArticleQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().published().search(query)

class Article(models.Model):
    #id = models.IntegerField() #pk
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    #photo = models.ImageField(upload_to='image/', blank=True, null=True)
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    title = models.CharField(max_length=240)
    slug = models.SlugField(unique=True) #hello world --> hello-world
    content = models.TextField(null=True, blank=True)
    publish_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = ArtileManager()

    class Meta:
        ordering = ['-publish_date','-timestamp','-updated']

    def get_absolute_url(self):
        return f"/news/{ self.id}/{self.slug}"

    def get_edit_url(self):
        return f"{ self.get_absolute_url()}/edit/"

    def get_delete_url(self):
        return f"{ self.get_absolute_url() }/delete/"
#3.28
#42
