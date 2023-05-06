from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.http.response import JsonResponse
from .models import DailyScore


# Create your views here.
@login_required
def index(request):

    return render(request,'Exercise/Exercise.html')

@login_required
def individual_exercise(request):

    return render(request, 'Exercise/Exercise1.html')

def get_score(request):
    return JsonResponse(list(DailyScore.objects.all().values()), safe=False)