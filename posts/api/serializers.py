from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    # highlight = serializers.HyperlinkedIdentityField(
    #     view_name='post-highlight', format='html')

    class Meta:
        model = Post
        fields = ('id', 'content')
