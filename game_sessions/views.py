from django.shortcuts import render,get_object_or_404
from django.views import generic
from .models import Post
from .forms import CommentForm






class Game_session_List(generic.ListView):
    queryset = Post.objects.all()
    #template_name = "post_list.html"
    template_name = "game_sessions/index.html"
    paginate_by = 3


    def post_description(request, post_id):

        queryset = Post.objects.filter()
        post = get_object_or_404(queryset, slug=post_id)
        comments = post.comments.all().order_by("-created_on")
        comment_count = post.comments.filter(approved=True).count()
        if request.method == "POST":
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.gamer_tag = request.user
                comment.post = post
                comment.save()
        comment_form = CommentForm()

        return render(request,
            "game_sessions/post_descripton.html",
            {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
            }
    )

    
