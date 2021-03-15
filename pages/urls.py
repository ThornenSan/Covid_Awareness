from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('details', views.hospitals_details, name='details'),
    path('contact', views.contact, name='contact'),
    path('register', views.register, name='register'),
]
