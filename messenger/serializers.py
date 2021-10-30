from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.HyperlinkedModelSerializer):
    post = serializers.HyperlinkedRelatedField(
        view_name='Post_detail', read_only=True)
    owner = serializers.ReadOnlyField(source='profile.username')


    class Meta:
        model = Post
        fields = ('picture', 'body', 'updated', 'created','owner','post','id')
