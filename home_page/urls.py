from . import views
from django.urls import path
from .views import indexPage

urlpatterns = [
    path('', views.indexPage, name='home'),
    #path('', data_print, name="home_list"),
]