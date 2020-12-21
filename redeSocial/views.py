from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from .models import *
from .serializers import *

class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'profile-list'

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'profile-detail'

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'post-list'

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'post-detail'

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-list'

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-detail'

class PostCommentList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCommentSerializer
    name = 'post-comment-list'

class PostCommentDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCommentSerializer
    name = 'post-comment-detail'

class ProfilePostList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfilePostSerializer
    name = 'profile-post-list'

class ProfilePostDetail(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfilePostSerializer
    name = 'profile-post-detail'

class ProfilePostsComments(APIView):
    name = 'profile-posts-comments'

    def get(self, request, format=None):
        profiles = Profile.objects.all()
        profile_list = []
        
        for profile in profiles:
            profile_status = {}
            profile_posts = 0
            post_comments = 0

            for post in Post.objects.filter(userId=profile.pk):
                profile_posts += 1
                for comment in Comment.objects.filter(postId=post.pk):
                    post_comments += 1

            profile_status['pk'] = profile.pk
            profile_status['name'] = profile.name
            profile_status['total_posts'] = profile_posts
            profile_status['total_comments'] = post_comments
            
            profile_list.append(profile_status)
        
        return Response(profile_list, status=status.HTTP_200_OK)

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'profiles' : reverse(ProfileList.name, request = request),
            'posts' : reverse(PostList.name, request=request),
            'profile-posts' : reverse(ProfilePostList.name, request=request),
            'post-comments' : reverse(PostCommentList.name, request=request),
            'profile-posts-comments': reverse(ProfilePostsComments.name, request=request),
        })