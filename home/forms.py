from .models import *
from django.forms import ModelForm

class PostForm(ModelForm):
    class Meta:
        model=Post
        fields=['title','author','time_stamp','content',]