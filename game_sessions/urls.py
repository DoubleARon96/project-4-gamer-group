from . import views
from django.urls import path

urlpatterns = [
    path('', views.Game_session_List.as_view(), name='home'),
]