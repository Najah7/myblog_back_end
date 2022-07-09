from rest_framework import serializers
from .models import Articles, Genre

class ArticlesSerializer(serializers.ModelSerializer):
    """記事用のシリアライザ"""
    class Meta:
        model = Articles
        fields = '__all__'
        extra_kwargs = {'title': {'required': True}}

class GenreSerializer(serializers.ModelSerializer):
    """ジャンル用のシリアライザ"""
    class Meta:
        model = Genre
        fields = '__all__'

