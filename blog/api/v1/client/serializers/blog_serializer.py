from rest_framework import serializers
from main.models import User, Article, Comment, Category

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 
            'name'
        ]

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id',
            'user',
            'text',
            'created_at',
            'article'
        ]


# I need to make so when article get called it also returns coments
class ArticleSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'text',
            'created_at',
            'category',
            'comments'
        ]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id', 
            'name',
            'description'
        ]