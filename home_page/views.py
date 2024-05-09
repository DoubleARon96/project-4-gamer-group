from django.shortcuts import render,get_object_or_404
from django.views import generic
from .models import HomePage

def home_list(request):
    """
    Renders the About page
    """
    try:
        home_page = HomePage.objects.get(gamer_tag="Aaron") 
    except HomePage.DoesNotExist:
        home_page= get_object_or_404

        content = {
            "home_page": home_page,
        }

        return render(request, "home_page/home_content_list.html", content)

#class Home_Page(generic.View):
#    queryset =()
#    template_name = "home_content/index.html"

#class Home_Page_List(View):
    #template_name = compile("home_page/templates/home_page/home_content_list.html",'<string>', 'exec')
    #def home(request):
    #    context = {'message': 'Hello, Django!'}
    #    return render(request, 'myapp/index.html', context)