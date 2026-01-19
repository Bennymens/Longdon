from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('menu/', views.menu, name='menu'),
    path('elements/', views.elements, name='elements'),
    path('contact_process/', views.contact_process, name='contact_process'),
]