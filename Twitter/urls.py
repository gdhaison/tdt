"""Twitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from apps.users import views as user_views
from django.contrib.auth import views as auth_views
from apps.posts.views import (ListPostView, CreatePostView)
from rest_framework import routers
from apps.api.views import PostListCreateAPIView, PostDetailUpdateAPIView

router = routers.SimpleRouter()
router.register('posts', PostListCreateAPIView)
router.register('posts', PostDetailUpdateAPIView)

urlpatterns = [
    path('admin/', admin.site.urls),
    url('posts/', include('apps.posts.urls', namespace='posts')),
    path('', ListPostView.as_view(), name='root'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('api/', include(router.urls)),
]
