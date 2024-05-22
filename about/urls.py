from . import views
from django.urls import path

urlpatterns = [
    path('about/', views.about_list, name='about'),
    path('<slug:story_id>/edit_stories/', views.edit_story, name='edit_stories'),
    #path('<slug:story_id>/delete_comment/',views.comment_delete, name='delete_comment'),
]