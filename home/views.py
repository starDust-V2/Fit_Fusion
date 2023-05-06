from django.shortcuts import render
from .models import Post

# Create your views here.
def landing(request):
    
    about_well_being = {
        0 : [["one.png","Learn to recognize the signs of mental distress.Take care of your mind as well as your body"]],
        1 : [["one.png","Seek help if you or someone you know is struggling. Engage in activities that promote mental well-being, such as meditation, mindfulness, and exercise"]],
        2 : [["one.png","Mental health issues can affect anyone regardless of age, gender, or background. Mental health problems can impact work, relationships, and overall quality of life"]],
        3 : [["one.png","Stigma and discrimination surrounding mental health can prevent people from seeking help. Early intervention and treatment can improve outcomes for those struggling with mental health issues"]]

    }

    context = {
        "css_url" : "css/landing.css",
        "well_being": about_well_being,
        'link_position': -1
        
    }

    return render(request,'home/landing.html',context)

def home(request):
    user_info = {
        "image_url" : "one.png",
        "name" : "John Doe",
        "bio" : "This is the bio for me if there's any. Cause I need a one dance. Got a hennessey in my hands"
    }

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
        "posts" : posts

    }
    return render(request,'home/home.html',context)


def chat(request):

    context ={
        "css_url" : "css/chat.css",
        'link_position': 1,
        "user": {"image_url" : "one.png",
        "name" : "John Doe",
        "bio" : "This is the bio for me if there's any. Cause I need a one dance. Got a hennessey in my hands" }  
    }
    return render(request,'home/chat.html',context)


def confessions(request):


    user_info = {
    "image_url" : "one.png",
    "name" : "John Doe",
    "bio" : "This is the bio for me if there's any. Cause I need a one dance. Got a hennessey in my hands"
}
    if request.method == "POST":
        content=request.POST["content"]
        author=request.user
        post_type=0
    posts=Post.objects.filter(post_type=0)
    
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
        "posts" : posts

    }
    return render(request,'home/confessions.html',context)