from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect, reverse
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

    viewbag = {"contents": content,
               "about_form": about_form}
    return render(request, "about/about_base.html", viewbag)


def about_form(request):
    content = aboutForm
    viewbag = {about_form: content}

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
def edit_story(request, id):
    """
    This function is to edit stories but still isn't fully incorporated
    """
    if request.method == "POST":
        post = get_object_or_404(AdminStory, id=id)
        about_form = aboutForm(data=request.POST, instance=post)

        if about_form.is_valid():
            if request.user.is_superuser:
                story = about_form.save(commit=False)
                story.approved = False
                story.save()
                messages.success(request, 'Story updated successfully!')
        else:
            messages.error(request,
                           f'Error updating story: {about_form.errors}')

    return redirect('about')


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
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('about_base', args=[id]))
