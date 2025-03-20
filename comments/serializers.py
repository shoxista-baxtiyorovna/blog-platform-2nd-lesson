from rest_framework import serializers
from .models import Comment
from posts.models import Post


class CommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()
    post = serializers.IntegerField(write_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'author_name', 'author_email', 'content', 'created_at', 'parent_comment', 'post', 'replies')

    def get_replies(self, instance):
        replies = instance.replies.all()
        return CommentSerializer(replies, many=True).data


    def create(self, validated_data):
        post_id = validated_data.pop('post')
        post = Post.objects.get(pk=post_id)
        comment = Comment.objects.create(
            post=post,
            **validated_data,
        )
        return comment