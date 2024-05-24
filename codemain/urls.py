
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path('summernote/', include('django_summernote.urls')),
    path("", include('home_page.urls'), name='home-urls'),
    path("", include('about.urls'), name='about-urls'),
    path("", include('game_sessions.urls'), name='game_sessions-urls'),

]
