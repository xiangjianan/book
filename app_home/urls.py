from django.urls import path, re_path
from app_home import views

urlpatterns = [
    path('home/', views.home),
    path('home_err/', views.home_err),
    path('publish/', views.publish),
    path('author/', views.author),
    re_path('(\d+)/change_author/', views.change_author),
    re_path('(\d+)/delete_book', views.delete_book),
    re_path('(\d+)/delete_auth', views.delete_auth),
    re_path('(\d+)/delete_pub', views.delete_pub),
    re_path('(\d+)/change_book', views.change_book),
    re_path('(\d+)/change_auth', views.change_auth),
    re_path('(\d+)/change_pub', views.change_pub),
    # path('add_pub/', views.add_pub),
    # path('add_book/', views.add_book),
    # path('add_auth/', views.add_auth),
]
