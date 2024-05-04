from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AdminStory (models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,)
    story_id = models.SlugField(max_length=200, unique=True)
    stories = models.TextField (unique=True)
    updated_on = models.DateTimeField(auto_now=True)