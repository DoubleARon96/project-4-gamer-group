from . import views
from django.urls import path
from .views import HomePage_View

urlpatterns = [
    path('', views.HomePageLoader, name='home'),
    path('<slug:my_slug>/', HomePage_View.as_view(), name='home_content'),
]