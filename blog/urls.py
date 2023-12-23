from django.urls import path
from . import views

name_app = 'blog'

urlpatterns = [
    path('', views.blog_home, name = 'blog_home'),
    path('single', views.blog_single, name = 'blog_single')

]