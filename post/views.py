from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.generics import get_object_or_404, CreateAPIView
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .models import Post
from .serializers import PostSerializer, UserSerializer

app_name = "posts"
class PostView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response({"posts": serializer.data})

    def post(self, request):
        post = request.data.get('post')
        serializer = PostSerializer(data=post)
        if serializer.is_valid(raise_exception=True):
            post_saved = serializer.save()
        return Response({"success": "Post '{}' created successfully".format(post_saved.title)})

    def put(self, request, pk):
        saved_post = get_object_or_404(Post.objects.all(), pk=pk)
        data = request.data.get('post')
        serializer = PostSerializer(instance=saved_post, data=data, partial=True)
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


class Like(APIView):
    def post(self, request, pk):
        post = get_object_or_404(Post.objects.all(), pk=pk)
        if post.likes.filter(id=pk):
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return Response({"success": "Post '{}' was liked by user '{}'".format(post.title, request.user.id)})


class UserCreate(CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class LoginView(APIView):
    permission_classes = ()

    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        token, created = Token.objects.get_or_create(user=user)
        if user:
            return Response({"token": token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)