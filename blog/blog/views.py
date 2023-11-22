from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import articleSerializer, tagSerializer, commentSerializer, categorySerializer
from main.models import article, tag, comment, category

class articleView(APIView):
    def get(self, request):
        articles = article.objects.all()
        serializer = articleSerializer(articles, many=True)
        return Response(serializer.data)
class tagView(APIView):
    def get(self, request):
        tags = tag.objects.all()
        serializer = tagSerializer(tags, many=True)
        return Response(serializer.data)
class commentView(APIView):
    def get(self, request):
        comments = comment.objects.all()
        serializer = commentSerializer(comments, many=True)
        return Response(serializer.data)
class categoryView(APIView):
    def get(self, request):
        categories = category.objects.all()
        serializer = categorySerializer(categories, many=True)
        return Response(serializer.data)