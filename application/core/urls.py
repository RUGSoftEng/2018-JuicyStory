"""core URL Configuration
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
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token
from django.contrib import admin
from django.urls import path, include
from .routers import router
from . import views

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/', include('database.urls')),
    path('api/get-token/', obtain_jwt_token),
    path('api/verify-token/', verify_jwt_token),
    path('docs/', include_docs_urls(title='Juicy Story API', public=False)),
    path('admin/', admin.site.urls, name='admins'),
    path('entry/', include('entry.urls')),
    path('iusers/', include('iusers.urls')),
    path('auth/', include('authentication.urls')),
    path('upload/<iusername>/', include('upload.urls')),
    path('incoming/<iusername>/', include('incoming.urls'), name='incoming'),
    path('statistics/<iusername>/', include('statistics.urls'), name='statistics'),
    path('<username>/', views.home, name='home'),
]

urlpatterns += staticfiles_urlpatterns()
