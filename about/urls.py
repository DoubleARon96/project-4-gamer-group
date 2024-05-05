from . import views
from django.urls import path

urlpatterns = [
    path('', views.about_list.as_view(), name='about'),
]