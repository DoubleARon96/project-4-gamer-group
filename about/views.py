from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from django.shortcuts import render, get_object_or_404,reverse
from django.http import HttpResponseRedirect
from django.contrib.admin.views.decorators import staff_member_required
from .models import AdminStory
from .forms import aboutForm

def about_list(request):
    """
    Renders the About page
    """
    
    content = AdminStory.objects.all
    about_form = aboutForm()
    if request.method == "POST":
            about_form = aboutForm(data=request.POST)
            if about_form.is_valid():
                about = about_form.save(commit=False)
                about.author = request.user
                about.stories
                about.save()
                messages.add_message(
                request, messages.SUCCESS,
        'story Is Just Going To Be Checked '
    )
    about_form = aboutForm()

    viewbag = { "contents": content,
               "about_form":about_form }
    return render(request, "about/about_base.html", viewbag)

def about_form(request):
    content = aboutForm
    viewbag = {about_form:content}

    if request.method == "POST":
            about_form = aboutForm(data=request.POST)
            if about_form.is_valid():
                about = about_form.save(commit=False)
                about.author = request.user
                about.stories
                about.save()
                messages.add_message(
                request, messages.SUCCESS,
        'story Is Just Going To Be Checked '
    )
    about_form = aboutForm()


    return render(request,
            "about_base",
            {
            "about_form": about_form,
            }
    )
    


@staff_member_required
def edit_story(request, id, gamer_tag):
    """
    this function is to edit stories but still isn't full incorporate
    """
    #this function lets you edit
    if request.method == "POST":

        queryset = AdminStory.objects.all()
        post = get_object_or_404(queryset, slug=id)
        stories = get_object_or_404(AdminStory, pk=id)
        aboutform = aboutform(data=request.POST, instance=stories)

        if post.is_valid() and gamer_tag == request.superuser:
            stories = id.save(commit=False)
            stories.post = post
            stories.approved = False
            stories.save()
                
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('about_base', args=[id]))

def story_delete(request, id):
    """
    view to delete comment
    """
    queryset = AdminStory.objects.filter()
    story = get_object_or_404(queryset, pk=id)

    if story.author == request.user:
        story.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('about_base', args=[id]))

   
