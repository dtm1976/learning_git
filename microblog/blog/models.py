from django.db import models
from django.shortcuts import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField(blank=True, db_index=True)
    publish = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("post_detail_url", kwargs={'slug': self.slug})

    def __str__(self):
        return self.title