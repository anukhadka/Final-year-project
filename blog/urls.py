from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('home/dashboard/', views.dashboard, name = 'dashboard'),
    path('home/', views.home, name = 'home'),
    path('add/blog/', views.add_blog, name ='add_blog'),
    path('blog/detail/<id>/', views.blog_details, name='blog_details'),
    path('blog/edit/<id>/', views.edit_blog, name='edit_blog'),
    path('blog/delete/<id>/', views.delete_blog, name='delete_blog'),
    path('accounts/signup/',views.user_registration,name='signup'),
]
