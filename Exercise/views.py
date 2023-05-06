from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'Exercise/Exercise.html')

def pushup(request):
    return render(request,'Exercise/pushup.html')
def curl(request):
    return render(request,'Exercise/curl1.html')
def squat(request):
    return render(request,'Exercise/squat1.html')

def individual_exercise(request):
    return render(request, 'Exercise/Exercise1.html')