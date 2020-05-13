from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, FormView
from django.contrib.messages.views import SuccessMessageMixin
from .models import Post
from .forms import CreatePostForm, CreateLikeForm

class ListPostView(ListView):
    model = Post

    def get(self, request, *args, **kwargs):
        template_name = "posts/list-posts.html"
        obj = {
          'posts': Post.objects.all().order_by('-id')
        }
        return render(request, template_name, obj)

    def post(self, request, *args, **kwargs):
        like_form = CreateLikeForm(data=request.POST).save()

        return redirect("root")

class CreatePostView(SuccessMessageMixin, CreateView):
    template_name = 'posts/create-post.html'
    form_class = CreatePostForm
    success_message = 'Create Post Successfully'
