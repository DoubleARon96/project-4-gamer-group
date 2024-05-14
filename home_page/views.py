from django.shortcuts import render,get_object_or_404
from .models import HomePage

#class HomePage_View(ListView):
     
def indexPage(request):
     return render(request, "home_page.html")

def data_print(request):
    data = HomePage.objects.all()
    contents = {"home_list": data}
    return render(request, 'home_page.html', contents)