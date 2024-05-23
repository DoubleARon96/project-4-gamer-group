from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AdminStory (models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE,)
    stories = models.TextField (unique=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    