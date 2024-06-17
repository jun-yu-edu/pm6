from django.urls import path
from articles import views

urlpatterns = [
    path('data/', views.data),
    path('json-data/', views.json_data),
    path('hello/', views.hello),
    path('random_data/<int:num>/', views.random_data),
    path('hello/<str:name>/', views.hello_name)
]
