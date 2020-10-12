from django.urls import path
from app_home import views

urlpatterns = [
    path('home/', views.home),
    path('home_err/', views.home_err),
    path('publish/', views.publish),
    path('author/', views.author),
    # path('add_pub/', views.add_pub),
    # path('add_book/', views.add_book),
    # path('add_auth/', views.add_auth),
]