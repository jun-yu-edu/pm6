from django.shortcuts import render
from articles.models import Article

from rest_framework.response import Response
from rest_framework.decorators import api_view
from articles.serializers import ArticleSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def article_list(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)

    return Response(serializer.data)
