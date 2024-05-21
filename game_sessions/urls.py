from . import views
from django.urls import path


urlpatterns = [
    path('game_sessions/', views.Game_session_List.as_view(), name='game_sessions'),
    path('<slug:post_id>/', views.Game_session_List.post_description, name='post_description'),
    #path('update_player_count/<slug:post_id>/', views.update_player_count, name='update_player_count'),
    path('update_player_count/<str:post_id>/', views.update_player_count, name='update_player_count'),
    path('<slug:post_id>/edit_comment/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    #path('<slug:slug>/edit_comment/<int:comment_id>',views.comment_edit, name='comment_edit'),
    path('<slug:post_id>/delete_comment/<int:comment_id>/',views.comment_delete, name='delete_comment'),
]