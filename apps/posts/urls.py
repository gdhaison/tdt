from django.urls import path
from apps.posts.views import (ListPostView, CreatePostView)

app_name = 'apps.posts'
urlpatterns = [
    path('', ListPostView.as_view(), name='list-posts'),
    path('create-post/', CreatePostView.as_view(), name='create-post')
]