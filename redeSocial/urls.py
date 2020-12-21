from django.urls import path, include
from .views import *

urlpatterns = [
    path('', ApiRoot.as_view(), name=ApiRoot.name),
    path('profiles/', ProfileList.as_view(), name=ProfileList.name),
    path('profiles/<int:pk>/', ProfileDetail.as_view()),
    path('posts/', PostList.as_view(), name=PostList.name),
    path('posts/<int:pk>/', PostDetail.as_view()),
    path('profile-posts/', ProfilePostList.as_view(), name=ProfilePostList.name),
    path('profile-posts/<int:pk>/', ProfilePostDetail.as_view()),
    path('posts-comments/', PostCommentList.as_view(), name=PostCommentList.name),
    path('posts-comments/<int:pk>/', PostCommentDetail.as_view(), name=PostCommentDetail.name),
    path('posts/<int:pk>/comments/', CommentList.as_view(), name=CommentList.name),
    path('posts/<int:pk>/comments/<int:comment_pk>/', CommentDetail.as_view(), name=CommentDetail.name),
    path('profile-posts-comments/', ProfilePostsComments.as_view(), name=ProfilePostsComments.name),

]