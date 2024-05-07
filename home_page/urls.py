from . import views
from django.urls import path

urlpatterns = [
    path('home/', views.Home_Page.as_view(), name='home')
    
]

