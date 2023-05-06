from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index,name='index'),
    path("pushup/", views.pushup,name='index'),
    path("curl", views.curl,name='index'),
    path("squat/", views.squat,name='index'),
    path("individual_exercise/", views.individual_exercise,name='individual_exercise')

    path("individual_exercise/", views.individual_exercise,name='individual_exercise'),
    path("get_score/", views.get_score, name='get_score')
]
