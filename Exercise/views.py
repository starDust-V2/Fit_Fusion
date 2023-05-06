from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request,'Exercise/Exercise.html')

def individual_exercise(request):

    return render(request, 'Exercise/Exercise1.html')