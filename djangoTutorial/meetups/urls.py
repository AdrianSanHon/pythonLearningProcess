from django.urls import path
from . import views

urlspatterns = [
    path("meetups", views.index) #our-domain/meetups

]