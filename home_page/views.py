from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views import generic


def HomePageLoader(request):
    return render(request, 'home_page.html')
