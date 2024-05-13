from . import views
from django.urls import path
from .views import HomePageLoader

urlpatterns = [
    #path('', HomePageView.as_view(), name='home'),
    #path('home/', views.HomePageView, name='home')
    path('home/', views.HomePageLoader, name='home'),
    
]

