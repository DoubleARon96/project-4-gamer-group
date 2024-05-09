from django.shortcuts import render
from django.views import generic
from .models import HomePage

def home_list(request):
    """
    Renders the About page
    """
    home_page = HomePage.objects.all(filter(1))

    return render(
        request,
        "home_page/home_content_list.html",
        {"home_page": HomePage},
    )

#class Home_Page(generic.View):
#    queryset =()
#    template_name = "home_content/index.html"

#class Home_Page_List(View):
    #template_name = compile("home_page/templates/home_page/home_content_list.html",'<string>', 'exec')
    #def home(request):
    #    context = {'message': 'Hello, Django!'}
    #    return render(request, 'myapp/index.html', context)