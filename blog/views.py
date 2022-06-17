from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "blog/index.html")

def page2(request):
    return render(request, "blog/page2.html")