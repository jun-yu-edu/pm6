from django.urls import path, include
from accounts import views

urlpatterns = [
    path('register/', views.register),
    path('me/', views.me)
]
