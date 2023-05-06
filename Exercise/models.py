from django.db import models
from django.contrib.auth.models import User
class UserScore(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    work_days=models.IntegerField()
    gap_days=models.IntegerField()
    streak=models.IntegerField()
    last_workout=models.DateTimeField()


class DailyScore(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now=True)
    score=models.IntegerField()
