from django.shortcuts import render, get_object_or_404,reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
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
                messages.add_message(
                request, messages.SUCCESS,
        'Comment Is Just Going To Be Checked '
    )
        comment_form = CommentForm()


        return render(request,
            "game_sessions/post_descripton.html",
            {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
            "joined_status":0,
            }
    )

def edit_comment(request, slug, comment_id,Post):
    """
    edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter()
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
                
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def delete_comment(request, post_id):
    post = get_object_or_404(Post, slug=post_id)

    if request.method == "POST":
        post.delete()
        slug = post_id
        messages.add_message(request, messages.SUCCESS, 'deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'Error updating comment!')
        
    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
    #        return redirect("post_list.html")  # Redirect to your list view
    #    return render(request, "your_template_for_delete_confirmation.html", {"post": post})
   