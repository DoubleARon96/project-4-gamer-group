from django.shortcuts import render
from django.views import generic
from .models import AdminStory


#class about_list(generic.ListView):
#    queryset = AdminStory.objects.all()
#    template_name = "about_list.html"

def about_list(request):
    """
    Renders the About page
    """
    content = AdminStory.objects.all()
    viewbag = { "contents": content }
    return render(request, "about/about_base.html", viewbag)
