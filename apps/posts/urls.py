from django.urls import path
from apps.posts.views import *

app_name = 'apps.posts'
urlpatterns = [
    path('create-comment/', ListPostView.as_view(), name='create-comment'),
    path('create-like/', ListPostView.as_view(), name='create-like'),
    path('create-post/', CreatePostView.as_view(), name='create-post'),
    path('delete-post/<post_id>', delete_like, name='delete-like'),
]