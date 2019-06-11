from django.urls import path
from .import views

urlpatterns = [
    #path('test/', views.getinput, name='input'),
    path('home/input/', views.getinput, name='getinput'),
    path('input/finalValues/', views.loadModel, name='loadModel'),

]