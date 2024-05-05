from django.shortcuts import render
from django.views import generic
from .models import Post


class Game_session_List(generic.ListView):
    queryset = Post.objects.all()
    template_name = "post_list.html"
#from django.http import HttpResponse
# Create your views here.

#def my_game_sessions (request):
#    return HttpResponse("Test!!!")