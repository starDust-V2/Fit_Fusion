from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing, name="landing-page"),
    path("home/",views.home,name="home"),
    path('chat/',views.chat,name="chat"),
    path('home/confessions/',views.confessions,name='confessions'),
]
