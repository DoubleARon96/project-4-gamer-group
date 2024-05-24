from django.shortcuts import render,get_object_or_404
from .models import HomePage


def indexPage(request):
    content = HomePage.objects.all()
    contents = {"contents": content,
                "title": "Welcome!!" }
    return render(request, 'home_page.html',contents)
