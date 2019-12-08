from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer

app_name = "posts"
class PostView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response({"posts": serializer.data})

    def post(self, request):
        post = request.data.get('post')
        serializer = ArticleSerializer(data=post)
        if serializer.is_valid(raise_exception=True):
            post_saved = serializer.save()
        return Response({"success": "Post '{}' created successfully".format(post_saved.title)})

    def put(self, request, pk):
        saved_post = get_object_or_404(Post.objects.all(), pk=pk)
        data = request.data.get('article')
        serializer = ArticleSerializer(instance=saved_post, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            post_saved = serializer.save()
        return Response({
            "success": "Post '{}' updated successfully".format(post_saved.title)
        })

    def delete(self, request, pk):
        post = get_object_or_404(Post.objects.all(), pk=pk)
        post.delete()
        return Response({
            "message": "Post with id `{}` has been deleted.".format(pk)
        }, status=204)
