"""blango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar

from django.conf import settings
from django.contrib import admin
from django.urls import path, include
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.index),
    path('index.html', blog.views.index, name="index"),
    path("post/<slug>/", blog.views.post_detail, name="blog-post-detail"),
    path('page2.html', blog.views.page2),
    path("ip/", blog.views.get_ip),
]

#Add DjDT on DEBUG mode only
if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]

from django.conf import settings
print(f"Time zone: {settings.TIME_ZONE}")