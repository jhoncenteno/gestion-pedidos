from django.urls import path
from app_contacto import views

urlpatterns = [

    path('', views.contacto, name='contacto'),


]