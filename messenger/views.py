
from rest_framework import generics  # <- import generics
from .models import Post
from .serializers import PostSerializer
from rest_framework import permissions
from messenger.permissions import IsOwnerOrReadOnly


class PostHistory(generics.ListCreateAPIView):
    # add code here
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # add code here
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permissions_classes = [IsOwnerOrReadOnly]
