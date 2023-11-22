from rest_framework import serializers
from main.models import article, tag, comment, category
class articleSerializer(serializers.ModelSerializer):
        model = article
        fields = ['id', 'title', 'text', 'created_at']
class tagSerializer(serializers.ModelSerializer):
        model = tag
        fields = ['id', 'title', 'created_at']
class commentSerializer(serializers.ModelSerializer):
        model = comment
        fields = ['id', 'text', 'created_at']
class categorySerializer(serializers.ModelSerializer):
        model = category
        fields = ['id', 'title', 'created_at']