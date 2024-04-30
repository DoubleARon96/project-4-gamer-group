"""
URL configuration for codemain project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from game_sessions import views as game_sessions_views
from about import views as about_views

urlpatterns = [
    path('game_sessions', game_sessions_views.my_game_sessions, name='game_sessions'),
    path('admin/', admin.site.urls),
    path('about', about_views.my_about, name='about'),
]
