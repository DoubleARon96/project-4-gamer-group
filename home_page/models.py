from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class HomePage (models.Model):
    slug = models.SlugField(max_length=200, unique=True, default="home_page")
    title = models.TextField(max_length=30, unique=True)
    content = models.TextField(max_length=300)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
