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
        ('Apex L', 'Apex Legends'),
        ('Forza M', 'Forza Motasports'),
        ('Forza H', 'Forza Horizon'),
        ('Dead By Daylight', 'Dead By Daylight')
    )

    post_id = models.SlugField(max_length=200, unique=True)
    title = models.CharField(max_length=200, unique=True)
    gamer_tag = models.ForeignKey(User, on_delete=models.CASCADE,
                                  db_column="gamer_tag", null=True)
    description = models.TextField(max_length=500, unique=True)
    datetime = models.DateTimeField()
    game = models.CharField(max_length=20, choices=GAME_CHOICES,
                            default='Other')
    player_count = models.IntegerField()
    updated_on = models.DateTimeField(auto_now=True)
    slug = models.SlugField(post_id, default=post_id)
    joined_status = models.BooleanField(player_count, default=False)

    class Meta:

        ordering = ["-updated_on"]

    def __str__(self):
        return f"{self.title} | Made by {self.gamer_tag}"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    gamer_tag = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.body} | Made by {self.gamer_tag}"
