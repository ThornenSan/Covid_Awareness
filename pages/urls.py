from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('details', views.hospitals_details, name='details'),
    path('contact', views.contact, name='contact'),
]
