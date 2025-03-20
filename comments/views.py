from rest_framework.views import APIView
from rest_framework.response import Response
from posts.models import Post
from .serializers import CommentSerializer


class CommentListCreateView(APIView):
    def get_object(self, slug):
        try:
            post = Post.objects.get(slug=slug)
        except Post.DoesNotExist as ex:
            return Response({
                'error': 'Post Not Found'
            }, status=404)
        return post

    def get(self, request, slug):
        post = self.get_object(slug)
        serializer = CommentSerializer(post.comments, many=True)
        return Response(serializer.data)

    def post(self, request, slug):
        post = self.get_object(slug)
        data = request.data.copy()
        data['post'] = post.id

        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
