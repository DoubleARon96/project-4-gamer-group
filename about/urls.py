from . import views
from django.urls import path

urlpatterns = [
    path('about/', views.about_list, name='about'),
    path('<slug:id>/edit_stories/', views.edit_story, name='edit_stories'),
    path('delete_story/<int:id>/',views.story_delete, name='delete_story'),
]