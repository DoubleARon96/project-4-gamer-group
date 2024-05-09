from django.shortcuts import render,get_object_or_404
from django.views import generic
from .models import Post



class Game_session_List(generic.ListView):
    queryset = Post.objects.all()
    #template_name = "post_list.html"
    template_name = "game_sessions/index.html"
    paginate_by = 3


    def post_description(request, post_id):

        queryset = Post.objects.filter()
        post = get_object_or_404(queryset, slug=post_id)

        return render(
            request,
            "game_sessions/post_descripton.html",
            {"post": post},
    )
