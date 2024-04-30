from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def my_game_sessions (request):
    return HttpResponse("Test!!!")