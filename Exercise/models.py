from django.db import models
from django.contrib.auth.models import User
class UserScore(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    work_days=models.IntegerField()
    gap_days=models.IntegerField()
    streak=models.IntegerField()
    last_workout=models.DateTimeField()
    def __str__(self):
        return self.user.username


class DailyScore(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now=True)
    score=models.IntegerField()
    def __str__(self):
            return (self.user,self.score)