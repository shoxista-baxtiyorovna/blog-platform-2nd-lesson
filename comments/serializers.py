from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    # replies = serializers.SerializerMethodfield()

    class Meta:
        model = Comment
        fields = ('id', 'author_name', 'author_email', 'content', 'created_at', 'parent_comment')

    # def get_replies(self, instance):
    #     return