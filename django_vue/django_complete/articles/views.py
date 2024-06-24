from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from accounts.serializers import UserSerializer


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
            return Response(serializer.data, status=201)





@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, id):
    if request.method == 'GET':
        article = Article.objects.get(id=id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        article = Article.objects.get(id=id) 
        data = request.data 

        serializer = ArticleSerializer(article, data=data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article = Article.objects.get(id=id)
        article.delete()
        return Response(status=204)

@api_view(['POST'])
def comment_list(request, id):
    data = request.data
    article = Article.objects.get(id=id)

    serializer = CommentSerializer(data=data)

    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data)
    
@api_view(['PUT', 'DELETE'])
def comment_detail(request, article_id, comment_id):
    comment = Comment.objects.get(id=comment_id)

    
    if request.method == 'PUT':
        data = request.data
        serializer = CommentSerializer(comment, data=data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=204)

