from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm


class Game_session_List(generic.ListView):
    queryset = Post.objects.all()
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
                    'Comment Is Just Going To Be Checked ')
        comment_form = CommentForm()

        return render(request,
                      "game_sessions/post_description.html",
                      {
                       "post": post,
                       "comments": comments,
                       "comment_count": comment_count,
                       "comment_form": comment_form,
                       "joined_status": 0,
                        }
                      )


def update_player_count(request, post_id, action):
    post = get_object_or_404(Post, slug=post_id)

    if action == 'increment':
        Post.player_count += 1
    elif action == 'decrement':
        Post.player_count -= 1

    post.save()
    return HttpResponseRedirect('/index.html/')


def edit_comment(request, comment_id, post_id):
    """
    This function is the view behind the edit function
    """
    if request.method == "POST":

        queryset = Post.objects.filter()
        post = get_object_or_404(queryset, slug=post_id)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.gamer_tag == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()

        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_description', args=[post_id]))


def comment_delete(request, post_id, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter()
    post = get_object_or_404(queryset, slug=post_id)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.gamer_tag == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_description', args=[post_id]))
