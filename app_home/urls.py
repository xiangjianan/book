from django.urls import path
from app_home import views

urlpatterns = [
    path('home/', views.home),
    path('publish/', views.publish),
    path('author/', views.author),
]