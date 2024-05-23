from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from django.shortcuts import render, get_object_or_404,reverse
from django.http import HttpResponseRedirect
from django.contrib.admin.views.decorators import staff_member_required
from .models import AdminStory
from .forms import aboutForm

class About (generic.ListView):
    queryset = AdminStory.objects.all()
    template = "about/about_base.html"
    paginate_by = 1
    def about_list(request):
        """
        Renders the About page
        """
        content = AdminStory.objects.all
        viewbag = { "contents": content }
        return render(request, "about/about_base.html", viewbag)

def about_form(request):
    content = aboutForm
    viewbag = {about_Form:content}

    if request.method == "POST":
            about_Form = aboutForm(data=request.POST)
            if about_Form.is_valid():
                about = about_Form.save(commit=False)
                about.author = request.user
                about.save()
                messages.add_message(
                request, messages.SUCCESS,
        'story Is Just Going To Be Checked '
    )
    about_Form = aboutForm()


    return render(request,
            "about_base",
            {
            "about_form": about_Form,
            }
    )
    


@staff_member_required
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

   
