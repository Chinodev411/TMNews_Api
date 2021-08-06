from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
  path('techmount/', views.NewsList.as_view(), name='news_list'),
  path('techmount/<int:pk>',
      views.NewsDetail.as_view(), name='news_detail'),
  path('comments/', views.CommentList.as_view(), name='comment_list'),
  path('comments/<int:pk>', views.CommentDetail.as_view(), name='comment_detail'),
]