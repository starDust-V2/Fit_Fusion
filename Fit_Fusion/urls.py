from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/",include("Users.urls")),
    path("", include('home.urls')),
    path("chats/",include('Chats.urls')),

    path("exercise/", include('Exercise.urls')),
    path("videochat/",include('VideoChat.urls')),
    path('analytics/',include('Analytics.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)