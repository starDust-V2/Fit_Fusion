from django.shortcuts import render

# Create your views here.
def landing(request):
    context = {
        'css_url' : "css/landing.css",
    }
    return render(request,'home/landing.html',context)

def home(request):
    context = {
        'css_url' : "css/home.css",
    }
    return render(request,'home/home.html',context)
