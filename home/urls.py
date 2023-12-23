from django.urls import path
from . import views


name_app = 'home'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('elements', views.elements, name = 'elements'),
    path('contact', views.contact, name = 'contact'),
    path('about', views.about, name = 'about'),

]