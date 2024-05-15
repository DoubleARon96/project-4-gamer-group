from django.shortcuts import render,get_object_or_404
from .models import HomePage

#class HomePage_View(ListView):
def indexPage(request):
    data = HomePage.objects.all()
    contents = {"contents": data}
    return render(request, 'home_page.html', contents )

def data_print(request):
    data = HomePage.objects.all()
    contents = {"contents": data}
    return render(request, 'home_page.html', {"contents": contents} )

from django.shortcuts import render
