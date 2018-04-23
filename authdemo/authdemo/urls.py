"""authdemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path, include
from .routers import router
from . import views

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls, name='admins'),
    path('users/', include('users.urls')),
    path('iusers/', include('iusers.urls')),
    path('authcode/', include('authcode.urls')),
    path('upload/<iusername>/', include('upload.urls')),
    path('incoming/<iusername>/', include('incoming.urls'), name='incoming'),
    path('<username>/', views.home, name='home'),
    path('stats/<access_token>/',include('stats.urls'),name = 'stats')
]

urlpatterns += staticfiles_urlpatterns()
