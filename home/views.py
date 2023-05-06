from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from Exercise.models import UserScore
# Create your views here.
def landing(request):
    
    about_well_being = {
        0 : [["images/one-landing.png","Take control of your physical and mental well-being with our comprehensive health and wellness app. Start your journey to a healthier, happier you with our easy-to-use app."]],
        1 : [["images/two-landing.png","Stay fit and healthy with our selection of exercises and pose tracking features. Get a personalized fitness analysis to track your progress and achieve your goals."]],
        2 : [["images/three-landing.png","Talk to physical and mental health experts through video calls and get the guidance you need. Find emotional support through our chat app and connect with strangers who can relate."]],
    }

    context = {
        "css_url" : "css/landing.css",
        "well_being": about_well_being,
        'link_position': -1
        
    }

    return render(request,'home/landing.html',context)

@login_required
def home(request):

    user_info = {
        "image_url" : "one.png",
        "name" : "John Doe",
        "bio" : "This is the bio for me if there's any. Cause I need a one dance. Got a hennessey in my hands"
    }
    top_users=UserScore.objects.order_by('-streak')[:5]
    # title author date_posted support report comment_json
    posts = [
        ["Title of the post","author1","2079 Jan 2 11:00pm", "Hello from the other side. I must have called a thousand times. To tell I'm sorry for everything that I have done. Hello from the outside. I need one dnace got a hennessey in my hands one more time for I go higher powers taking a hold on me ",1,1,{}],
        ["Title of the post","author1","2079 Jan 2 11:00pm", "Hello from the other side. I must have called a thousand times. To tell I'm sorry for everything that I have done. Hello from the outside. I need one dnace got a hennessey in my hands one more time for I go higher powers taking a hold on me ",1,1,{}],
        ["Title of the post","author1","2079 Jan 2 11:00pm", "Hello from the other side. I must have called a thousand times. To tell I'm sorry for everything that I have done. Hello from the outside. I need one dnace got a hennessey in my hands one more time for I go higher powers taking a hold on me ",1,1,{}],
        ["Title of the post","author1","2079 Jan 2 11:00pm", "Hello from the other side. I must have called a thousand times. To tell I'm sorry for everything that I have done. Hello from the outside. I need one dnace got a hennessey in my hands one more time for I go higher powers taking a hold on me ",1,1,{}],
        ["Title of the post","author1","2079 Jan 2 11:00pm", "Hello from the other side. I must have called a thousand times. To tell I'm sorry for everything that I have done. Hello from the outside. I need one dnace got a hennessey in my hands one more time for I go higher powers taking a hold on me ",1,1,{}],
        ["Title of the post","author1","2079 Jan 2 11:00pm", "Hello from the other side. I must have called a thousand times. To tell I'm sorry for everything that I have done. Hello from the outside. I need one dnace got a hennessey in my hands one more time for I go higher powers taking a hold on me ",1,1,{}],
    ]
    context = {
        'link_position': 0,
        "css_url" : "css/home.css",
        "user": user_info,
        "posts" : posts,
        "top_users" : top_users,

    }
    return render(request,'home/home.html',context)

@login_required
def chat(request):

    context ={
        "css_url" : "css/chat.css",
        'link_position': 1,
        "user": {"image_url" : "one.png",
        "name" : "John Doe",
        "bio" : "This is the bio for me if there's any. Cause I need a one dance. Got a hennessey in my hands" }  
    }
    return render(request,'Chats/index.html',context)

@login_required
def confessions(request):


    user_info = {
    "image_url" : "one.png",
    "name" : "John Doe",
    "bio" : "This is the bio for me if there's any. Cause I need a one dance. Got a hennessey in my hands"
    }
    if request.method == "POST":
        content=request.POST["content"]
        author=request.user
        title=request.POST["title"]
        user_post=Post(title=title,author=author,content=content,post_type=0)
        user_post.save()

        return redirect('confessions')
    
    posts=Post.objects.filter(post_type=0).reverse()
    context = {
        'link_position': 0,
        "css_url" : "css/home.css",
        "user": user_info,
        "posts" : posts

    }
 
    return render(request,'home/confessions.html',context)