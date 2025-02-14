from django.utils import timezone
from blog.models import Post
from django.shortcuts import render, get_object_or_404, redirect
from blog.forms import CommentForm
import logging
from django.views.decorators.cache import cache_page #Cach decorator
from django.views.decorators.vary import vary_on_headers


logger = logging.getLogger(__name__)

# Create your cached views here.
#@cache_page(300)
#@vary_on_headers("Cookie")
#def index(request):
#    from django.http import HttpResponse
#    return HttpResponse(str(request.user).encode("ascii"))

# Create your views here.
def index(request):
    # Optimized .difer() .select_relared -65% of the query time
    #posts = Post.objects.filter(published_at__lte=timezone.now()).select_related("author")\
    #    .defer("created_at","modified_at")
    #Optimized select_related -40% of the query time
    posts = Post.objects.filter(published_at__lte=timezone.now()).select_related("author")\
        .defer("created_at","modified_at")
    
    logger.debug("Got %d posts", len(posts))
    return render(request, "blog/index.html", {"posts": posts})

#Get you current IP addresss
def get_ip(request):
  from django.http import HttpResponse
  return HttpResponse(request.META['REMOTE_ADDR'])

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user.is_active:
        if request.method == "POST":
            comment_form = CommentForm(request.POST)

            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.content_object = post
                comment.creator = request.user
                comment.save()
                logger.info("Created comment on Post %d for user %s", post.pk, request.user)
                return redirect(request.path_info)
        else:
            comment_form = CommentForm()
    else:
        comment_form = None
    return render(
        request, "blog/post-detail.html", {"post": post, "comment_form": comment_form}
    )

def page1(request):
    return render(request, "blog/index.html")

def page2(request):
    return render(request, "blog/page2.html")