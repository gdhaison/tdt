from django.urls import path
from apps.posts.views import (ListPostView, CreatePostView)

app_name = 'apps.posts'
urlpatterns = [
    path('create-like/', ListPostView.as_view(), name='create-like'),
    path('create-post/', CreatePostView.as_view(), name='create-post')
]