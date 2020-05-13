from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, FormView
from django.contrib.messages.views import SuccessMessageMixin
from .models import *
from .forms import CreatePostForm, CreateLikeForm, CreateCommentForm

class ListPostView(ListView):
    model = Post

    def get(self, request, *args, **kwargs):
        template_name = "posts/list-posts.html"
        posts = Post.objects.all().order_by('-id')
        liked = []
        for post in posts:
            if request.user.id in list(post.like_set.values_list('user_id', flat=True)):
                liked.append(post.id)
        get_like_id = []
        get_like_id = Post
        obj = {
          'posts': posts,
          'liked': liked
        }
        return render(request, template_name, obj)

    def post(self, request, *args, **kwargs):
        if request.path == "/posts/create-like/":
            like_form = CreateLikeForm(data=request.POST).save()
        else:
            comment_form = CreateCommentForm(data=request.POST).save()

        return redirect("root")

class CreatePostView(SuccessMessageMixin, CreateView):
    template_name = 'posts/create-post.html'
    form_class = CreatePostForm
    success_message = 'Create Post Successfully'

def delete_like(request, post_id):
    like = Like.objects.filter(user_id=request.user.id, post_id=post_id)
    like.delete()
    return redirect("root")
