from django.urls import include, path
from rest_framework import routers
from .views import articleView, tagView, commentView, categoryView

routers = routers.DefaultRouter()
routers.register(r'articles', articleView)
routers.register(r'tags', tagView)
routers.register(r'comments', commentView)
routers.register(r'categories', categoryView)

urlpatterns = [
    path('articles/', articleView.as_view()),
    path('tags/', tagView.as_view()),
    path('comments/', commentView.as_view()),
    path('categories/', categoryView.as_view()),
    path('api/', include(routers.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]