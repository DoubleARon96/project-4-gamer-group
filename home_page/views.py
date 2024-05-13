from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.views import generic


class HomePage(generic):
    
      def __init__(self):
          template = loader.get_template('home_content_list.html')
          return HttpResponse(template.render())
