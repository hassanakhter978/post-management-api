from rest_framework.response import Response
from posts.models import Post
from posts.serializer import PostSerializer
from rest_framework.views import APIView


# Create your views here.


class PostAPIView(APIView):

    def get(self, request):
        post_objects = Post.objects.all()
        serializer = PostSerializer(post_objects, many=True)
        return Response({'Status': 200, 'payload': serializer.data})

    def post(self, request):
        serializer = PostSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({"Status": 403, "errors": serializer.errors, "message": "The serializer is invalid"})

        serializer.save()
        return Response({"Status": 200, "payload": serializer.data, "message": "Your new Data is saved"})

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response({"message": "Not Found"})

    def put(self, request, pk):

        post_object = self.get_object(pk)
        serializer = PostSerializer(post_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Status": 200, 'payload': serializer.data, "message": "Your data is updated"})

        return Response({'Status': 400, 'error': serializer.errors})

    def delete(self, request, pk):
        post_object = self.get_object(pk)
        post_object.delete()
        return Response({"message": 'The post is deleted'})
