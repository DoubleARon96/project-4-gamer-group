from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.views.generic.base import TemplateView
from .models import HomePage


class HomePageView(TemplateView):
    template_name = "home_content_list.html"

    def get_content(self, **kwargs):
        context = super().get_content(all)
        context["latest_articles"] = HomePage.objects.content()
        return context

#def home_list(request):
 #   """
 #   Renders the About page
 #   """
 #   try:
  #      home_page = HomePage.objects.get(gamer_tag="Aaron") 
  #  except HomePage.DoesNotExist:
  #      home_page= get_object_or_404
#
 #       content = {
  #          "home_page": home_page,
   #     }
#
 #       return render(request, "home_page/home_content_list.html", content)

#class Home_Page(generic.View):
#    queryset =()
#    template_name = "home_content/index.html"