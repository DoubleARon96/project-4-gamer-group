from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomePage.objects.all, name='home')
    
]

