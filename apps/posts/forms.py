from django import forms
from .models import Post, Like, Comment

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'user', ]

class CreateLikeForm(forms.ModelForm):
    class Meta:
        model = Like
        fields = ['user', 'post', ]

class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user', 'content', 'post', ]
