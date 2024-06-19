from django.shortcuts import render
from articles.models import Article

from rest_framework.response import Response
from rest_framework.decorators import api_view
from articles.serializers import ArticleSerializer

@api_view(['GET', 'POST'])
def article_list(request):

    if request.method == 'GET':
    
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        
        return Response(serializer.data)
    
    
    elif request.method == 'POST':
    
        data = request.data
        serializer = ArticleSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            
            return Response(serializer.data)



@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, id):

    if request.method == 'GET':
    
        article = Article.objects.get(id=id)
        serialzer = ArticleSerializer(article)

        return Response(serialzer.data)
    
    
    elif request.method == 'PUT':
        data = request.data
        article = Article.objects.get(id=id)
        serialzer = ArticleSerializer(article, data=data, partial=True)

        if serialzer.is_valid(raise_exception=True):
            serialzer.save()
            
            return Response(serialzer.data)
            
            
    elif request.method == 'DELETE':
    
        article = Article.objects.get(id=id)
        article.delete()
        
        return Response(status=204)