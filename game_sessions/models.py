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
    gamer_tag = models.ForeignKey(User, on_delete=models.CASCADE, db_column="gamer_tag", null=True)
    description = models.TextField(max_length=500, unique=True)
    datetime = models.DateTimeField()
    game = models.CharField(max_length=20, choices=GAME_CHOICES, default='Other')
    player_count = models.IntegerField()
    updated_on = models.DateTimeField(auto_now=True)
    slug = models.SlugField(post_id, default=post_id)

    class Meta:
        ordering = ["-updated_on"]

    def __str__(self):
        return f"{self.title} | Made by {self.gamer_tag}"
    
    #class JoinSession(models.Model):
    #game = models.ForeignKey(Game, on_delete=models.CASCADE)
    #available_spaces = models.PositiveIntegerField()
    # Other fields as needed (e.g., session name, date, etc.)
    # def join_session(request, session_id):
    #session = JoinSession.objects.get(pk=session_id)
    #if session.available_spaces > 0:
    #    session.available_spaces -= 1
    #    session.save()
        # Add the user to the session (e.g., create a Player object)
        # Redirect to the session details page
    #else:
        # Handle case when no available spaces
        # Redirect to an error page or display a message


    #This is to help make it count the player number and let you join and leave
    #class InheritActionForm(forms.ModelForm):
    #type = forms.ChoiceField(choices=INHERIT_ACTION_TYPE)  # Use your custom choices here

    #class Meta:
    #    model = InheritAction

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    title = models.CharField(max_length=200, unique=True, default="title")
    gamer_tag = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | Made by {self.gamer_tag}"