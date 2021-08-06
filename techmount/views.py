from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import News, Comment
from .serializers import NewsSerializer, CommentSerializer
# from rest_framework import permissions
# from techmount.permissions import IsOwnerOrReadOnly


class NewsList(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    # permission_classes = [IsOwnerOrReadOnly]

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # permission_classes = [IsOwnerOrReadOnly]


