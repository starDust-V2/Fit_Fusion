from django.shortcuts import render

# Create your views here.
def analytics(request):
    context = {

    }
    return render(request,'Analytics/home.html',context)