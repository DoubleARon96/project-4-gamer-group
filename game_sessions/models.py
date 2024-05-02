from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    post_id = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=200, unique=True)
    gamer_tag = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=400, unique=True)
    datetime = models.DateTimeField()
    game = models.Choices()
    player_count = models.IntegerField(max_length=2)