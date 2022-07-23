import json
from http import HTTPStatus

from django.http import JsonResponse, HttpResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from blog.api.serializers import PostSerializer
from rest_framework.decorators import api_view

from blog.models import Post

from http import HTTPStatus

from django.urls import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from blog.api.serializers import PostSerializer
from blog.models import Post


@api_view(["GET", "POST"])
def post_list(request, format=None):
    if request.method == "GET":
        posts = Post.objects.all()
        return Response({"data": PostSerializer(posts, many=True).data})
    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            post = serializer.save()
            return Response(
                status=HTTPStatus.CREATED,
                headers={"Location": reverse("api_post_detail", args=(post.pk,))},
            )
        return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def post_detail(request, pk, format=None):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=HTTPStatus.NOT_FOUND)

    if request.method == "GET":
        return Response(PostSerializer(post).data)
    elif request.method == "PUT":
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=HTTPStatus.NO_CONTENT)
        return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)
    elif request.method == "DELETE":
        post.delete()
        return Response(status=HTTPStatus.NO_CONTENT)

""" Old version without decorator
@csrf_exempt
def post_list(request):
    if request.method == "GET":
        posts = Post.objects.all()
        return JsonResponse({"data": PostSerializer(posts, many=True).data})
    elif request.method == "POST":
        #Create new record
        post_data = json.loads(request.body)
        serializer = PostSerializer(data=post_data)
        serializer.is_valid(raise_exception=True)
        post = serializer.save()
        return HttpResponse(
            status=HTTPStatus.CREATED,
            headers={"Location": reverse("api_post_detail", args=(post.pk,))},
        )

    return HttpResponseNotAllowed(["GET", "POST"])


@csrf_exempt
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "GET":
        #Get record with pk
        return JsonResponse(PostSerializer(post).data)
    elif request.method == "PUT":
        #Update record pk
        post_data = json.loads(request.body)
        serializer = PostSerializer(post, data=post_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return HttpResponse(status=HTTPStatus.NO_CONTENT)
    elif request.method == "DELETE":
        #Delete record pk
        post.delete()
        return HttpResponse(status=HTTPStatus.NO_CONTENT)

    return HttpResponseNotAllowed(["GET", "PUT", "DELETE"])
    """