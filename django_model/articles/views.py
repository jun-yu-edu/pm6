from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from articles.models import Article

# def create(request):

#     article = Article(title='제목', content='내용')
#     article.save()

#     return HttpResponse(article )


# def read(request):

#     articles = Article.objects.all()

#     return HttpResponse(articles)


# def read_id(request, id):

#     article = Article.objects.get(id=id)

#     return HttpResponse(article)