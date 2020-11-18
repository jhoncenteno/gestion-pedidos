from django.urls import path
from app_blog import views

urlpatterns = [

    path('', views.blog, name='blog'),
    path('nacionales/', views.nacionales, name='nacionales'),
    path('internacionales/', views.internacionales, name='internacionales'),

]