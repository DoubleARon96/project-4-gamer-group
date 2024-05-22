from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from django.shortcuts import render, get_object_or_404,reverse
from django.http import HttpResponseRedirect
from .models import AdminStory
from .forms import aboutForm


def about_list(request):
    """
    Renders the About page
    """
    content = AdminStory.objects.all()
    viewbag = { "contents": content }
    return render(request, "about/about_base.html", viewbag)

def about_form(request):
    content = aboutForm
    viewbag = {about_form:content}
    return render(request, "about/about_base.html", viewbag)



def edit_story(request, story_id, gamer_tag):
    #this function lets you edit
    if request.method == "POST":

        queryset = AdminStory.objects.all()
        post = get_object_or_404(queryset, slug=story_id)
        stories = get_object_or_404(AdminStory, pk=story_id)
        aboutForm = aboutForm(data=request.POST, instance=stories)

        if post.is_valid() and gamer_tag == request.superuser:
            stories = story_id.save(commit=False)
            stories.post = post
            stories.approved = False
            stories.save()
                
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('about_base', args=[story_id]))

#def comment_delete(request, post_id, comment_id):
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
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_description', args=[post_id]))

   
