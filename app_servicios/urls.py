from django.urls import path
from app_servicios import views

urlpatterns = [

    path('', views.servicios, name='servicios'),
]
