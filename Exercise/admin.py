from django.contrib import admin

# Register your models here.
from .models import *

class UserScoreAdmin(admin.ModelAdmin):
    list_display=('user','work_days','gap_days','streak','last_workout')

admin.site.register(UserScore,UserScoreAdmin) 

class DailyScoreAdmin(admin.ModelAdmin):
    list_display=('user','date','score')
admin.site.register(DailyScore,DailyScoreAdmin) 