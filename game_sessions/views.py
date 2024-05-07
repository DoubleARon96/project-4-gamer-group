from django.shortcuts import render
from django.views import generic
from .models import Post


class Game_session_List(generic.ListView):
    queryset = Post.objects.all()
    #template_name = "post_list.html"
    template_name = "game_sessions/index.html"
    paginate_by = 3
