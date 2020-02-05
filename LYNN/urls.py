"""LYNN URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from TechChat import views
from TechChat.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls')),
    path('signup/', include('Register.urls')),
    path('chat/', include('Chat.urls')),
    path('techchat/', include('TechChat.urls')),
    path('', include("django.contrib.auth.urls")),
    path('requests/', include('Request.urls')),
    url(r'^view_users/$', views.view_users),
    url(r'^save_msg/$', views.save_msg),
    url(r'^get_chat/$', views.get_chat),
    url(r'^view_msg/$', views.view_msg),
    url(r'^index', index, name='index'),
]