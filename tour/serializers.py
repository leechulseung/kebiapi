from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('pk','author','title','contentid','created_at','updated_at')
        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }

class CommentSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False, max_length=None,
                        allow_empty_file=True, use_url=True, default=None)
    
    class Meta:
        model = Comment
        fields = ('pk','post','author', 'msg', 'image','created_at','updated_at')
        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }