from rest_framework import serializers
from .models import User, BlogPost, Comment, LikesDislikes

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'role']
        extra_kwargs = {'password': {'write_only': True}}

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'author', 'published_date', 'status']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'user', 'content', 'date_created']

class LikesDislikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikesDislikes
        fields = ['id', 'post', 'comment', 'user', 'reaction']
