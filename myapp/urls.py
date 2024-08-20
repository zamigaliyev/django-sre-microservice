from django.urls import path
from .views import my_view

urlpatterns = [
    path('api/v1/resource/', my_view),
]
