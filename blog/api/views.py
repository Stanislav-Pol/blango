from rest_framework import generics

from blog.api.serializers import PostSerializer
from blog.models import Post

from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from blog.api.permissions import AuthorModifyOrReadOnly, IsAdminUserForObject

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    #List of the allowed authentication methods
    #authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    #Allow only author make dange operation
    #Also allow to admin user make changes
    permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]
    #List of the allowed authentication methods
    #authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    #authentication_classes = [SessionAuthentication,]
