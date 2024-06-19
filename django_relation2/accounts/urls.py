from django.urls import path, include
from accounts import views

urlpatterns = [
    path('register/', views.register),
    path('me/', views.me),

    path('me/articles/', views.my_articles),
    
    path('bookmarks/<int:article_id>/', views.bookmark_article),
    path('me/bookmarked_articles/', views.bookmarked_articles )

]
