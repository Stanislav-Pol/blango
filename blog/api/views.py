from rest_framework import generics

from blog.api.serializers import PostSerializer
from blog.models import Post

from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    #List of the allowed authentication methods
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    #List of the allowed authentication methods
    #authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    authentication_classes = [SessionAuthentication,]
