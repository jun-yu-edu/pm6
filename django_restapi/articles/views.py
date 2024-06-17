from django.shortcuts import render
from articles.models import Article

from rest_framework.response import Response
from rest_framework.decorators import api_view
from articles.serializers import ArticleSerializer

@api_view(['GET', 'POST'])
def article_list(request):
    pass




@api_view([])
def article_detail(request, id):
    pass