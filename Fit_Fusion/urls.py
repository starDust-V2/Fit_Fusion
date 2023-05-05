from django.contrib import admin
<<<<<<< HEAD
=======
from django.conf import settings
from django.conf.urls.static import static
>>>>>>> ce4070e994bcf44a67b4954f1d02499cfb9cff96
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
<<<<<<< HEAD
    path("users/",include("Users.urls")),
=======
    path("", include('home.urls')),
>>>>>>> ce4070e994bcf44a67b4954f1d02499cfb9cff96
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)