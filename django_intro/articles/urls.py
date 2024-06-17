from django.urls import path
from articles import views

urlpatterns = [
    path('data/', views.data),
    # path('json-data/', views.json_data),
    # path('random_data/<int:num>/', views.random_data),
]
