"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
from rest_framework import routers
from .ViewSet import articleViewSet, tagViewSet, commentViewSet, categoryViewSet

routers = routers.DefaultRouter()
routers.register(r'articles', articleViewSet)
routers.register(r'tags', tagViewSet)
routers.register(r'comments', commentViewSet)
routers.register(r'categories', categoryViewSet)

urlpatterns = [
    path('', include(routers.urls)),
    path('articles/', articleViewSet.as_view({'get': 'title'})),
    path('tags/', tagViewSet.as_view({'get': 'title'})),
    path('comments/', commentViewSet.as_view({'get': 'text'})),
    path('categories/', categoryViewSet.as_view({'get': 'title'})),
    path('api/', include(routers.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
