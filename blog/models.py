from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.utils import timezone
from django.db import models

# Create your models here.

class Post(models.Model):
 class Status(models.TextChoices):
    DRAFT = 'DF', 'Draft'
    PUBLISHED = 'PB', 'Published'

 title = models.CharField(max_length=250)
 slug = models.SlugField(max_length=250)
 body = models.TextField()
 publish = models.DateTimeField(default=timezone.now)
 created = models.DateTimeField(auto_now_add=True)
 updated = models.DateTimeField(max_length=250)
 status = models.CharField(max_length=2,
                           choices=Status.choices,
                           default=Status.DRAFT)
 author = models.ForeignKey(User,
                            on_delete=models.CASCADE,
                            related_name="blog_posts")
 
 
 class PublishedManager(models.Manager):
   def get_queryset(self):
     return super().get_queryset()\
            .filtrer(status=Post.Status.PUBLISHED)