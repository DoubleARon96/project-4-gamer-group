from . import views
from django.urls import path

urlpatterns = [
    path('game_sessions/', views.Game_session_List.as_view(), name='game_sessions'),
]