from rest_framework import serializers
from .models import News, Comment

class NewsSerializer(serializers.HyperlinkedModelSerializer):
    comments = serializers.HyperlinkedRelatedField(view_name='comment_detail', many=True, read_only=True)

    news_url = serializers.ModelSerializer.serializer_url_field(view_name='news_detail')

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = News
        fields = ('id', 'author', 'title', 'description', 'url', 'source', 'published', 'comments', 'news_url', 'owner')

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    news = serializers.HyperlinkedRelatedField(view_name='news_detail', read_only=True)

    news_id = serializers.PrimaryKeyRelatedField(queryset=News.objects.all(), source='news')

    news_author = serializers.SlugRelatedField(queryset=News.objects.all(), slug_field='author', source='news')

    owner = serializers.ReadOnlyField(souce='owner.username')

    class Meta: 
        model = Comment
        fields = ('news', 'news_id', 'title', 'body', 'timestamp', 'news_author', 'owner')
        