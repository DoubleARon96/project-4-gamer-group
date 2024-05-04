from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    """
    this is the post class this lets admins and users with right authority to 
    make a post
    """
    GAME_CHOICES = (
        ('Halo', 'Halo'),
        ('Hell Divers 2', 'Hell Divers 2'),
        ('VR Chat', 'VR Chat'),
        ('Call Of Duty', 'Call Of Duty'),
        ('Other', 'Other'),
    )


    post_id = models.SlugField(max_length=200, unique=True)
    title = models.CharField(max_length=200, unique=True)
    gamer_tag = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=500, unique=True)
    datetime = models.DateTimeField()
    game = models.CharField(max_length=20, choices=GAME_CHOICES, default='Other')
    player_count = models.IntegerField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
