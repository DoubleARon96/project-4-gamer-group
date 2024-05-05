from django.shortcuts import render
from django.views import generic
from .models import AdminStory


class about_list(generic.ListView):
    queryset = AdminStory.objects.all()
    template_name = "about_list.html"
