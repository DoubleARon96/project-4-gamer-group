from django.shortcuts import render
from django.views import generic
from django.views import View



class Home_Page(generic.View):
    queryset =()
    template_name = "home_content/index.html"

#class Home_Page_List(View):
    #template_name = compile("home_page/templates/home_page/home_content_list.html",'<string>', 'exec')
    #def home(request):
    #    context = {'message': 'Hello, Django!'}
    #    return render(request, 'myapp/index.html', context)