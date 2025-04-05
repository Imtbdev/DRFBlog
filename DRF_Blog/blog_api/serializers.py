from rest_framework import serializers
from .models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "author", "text", "created_on", "post"]
        read_only_fields = ["id", "created_on", "author"]


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "slug",
            "author",
            "updated_on",
            "content",
            "created_on",
            "status",
            "comments",
        ]
        read_only_fields = ["id", "created_on", "updated_on", "author", "slug"]
