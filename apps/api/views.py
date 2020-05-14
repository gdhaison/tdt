from django.shortcuts import render

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,)
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from apps.posts.models import *

class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class PostDetailUpdateAPIView(viewsets.GenericViewSet, RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    look_field = 'id'

class PostListCreateAPIView(viewsets.GenericViewSet, ListCreateAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.all()

