from django import forms
from .models import Post, Like

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'user', ]

class CreateLikeForm(forms.ModelForm):
    class Meta:
        model = Like
        fields = ['user', 'post', ]
