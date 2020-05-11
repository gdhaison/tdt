from django.conf.urls import url, include
from apps.posts.views import ListPostView

app_name = 'apps.posts'
urlpatterns = [
    url('', ListPostView.as_view(), name='list-posts'),
]