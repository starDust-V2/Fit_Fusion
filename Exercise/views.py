from django.shortcuts import render
from django.http.response import JsonResponse
from .models import DailyScore

# Create your views here.
def index(request):

    return render(request,'Exercise/Exercise.html')

def individual_exercise(request):

    return render(request, 'Exercise/Exercise1.html')

def get_score(request):
    return JsonResponse(list(DailyScore.objects.all().values()), safe=False)