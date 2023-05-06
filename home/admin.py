from django.contrib import admin

from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display=('post_type','title','author','content','time_stamp')

admin.site.register(Post,PostAdmin)