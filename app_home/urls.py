from django.urls import path, re_path
from app_home import views

urlpatterns = [
    path('home/', views.home),
    path('home_err/', views.home_err),
    path('publish/', views.publish),
    path('author/', views.author),
    # 超链接
    re_path('(\d+)/pub_info/', views.pub_info),
    re_path('(\d+)/auth_info/', views.auth_info),
    # 删除
    re_path('(\d+)/delete_book', views.delete_book),
    re_path('(\d+)/delete_auth', views.delete_auth),
    re_path('(\d+)/delete_pub', views.delete_pub),
    # 修改
    re_path('(\d+)/change_book', views.change_book),
    re_path('(\d+)/change_auth', views.change_auth),
    re_path('(\d+)/change_pub', views.change_pub),
]
