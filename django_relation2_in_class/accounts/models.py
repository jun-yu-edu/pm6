from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    likes = models.ManyToManyField("articles.Article", related_name="liked_users")
    loves = models.ManyToManyField("articles.Article", related_name="love_users")
    bookmarks = models.ManyToManyField("articles.Article", related_name="bookmark_users")
    pass
