from rest_framework import viewsets
from main.models import article, tag, comment, category
from .serializers import articleSerializer, tagSerializer, commentSerializer, categorySerializer
class articleViewSet(viewsets.ModelViewSet):
    queryset = article.objects.all()
    serializer_class = articleSerializer
    basename = 'article'
class tagViewSet(viewsets.ModelViewSet):
    queryset = tag.objects.all()
    serializer_class = tagSerializer
    basename = 'tag'
class commentViewSet(viewsets.ModelViewSet):
    queryset = comment.objects.all()
    serializer_class = commentSerializer
    basename = 'comment'
class categoryViewSet(viewsets.ModelViewSet):
    queryset = category.objects.all()
    serializer_class = categorySerializer
    basename = 'category'