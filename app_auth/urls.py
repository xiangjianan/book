from django.urls import path
from app_auth import views

urlpatterns = [
    path('', views.login),
    path('login/', views.login),
    path('logout/', views.logout),
    path('reg/', views.reg),
    path('reg_success/', views.reg_success),
]
