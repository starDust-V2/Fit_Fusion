from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index,name='index'),
    path("individual_exercise/", views.individual_exercise,name='individual_exercise')

]
