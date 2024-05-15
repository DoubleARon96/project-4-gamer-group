from . import views
from django.urls import path


urlpatterns = [
    path('game_sessions/', views.Game_session_List.as_view(), name='game_sessions'),
    path('<slug:post_id>/', views.Game_session_List.post_description, name='post_description'),
    #path('<slug:post_id>/', views.Game_session_List.post_description, name='post_description'),
]