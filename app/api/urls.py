from django.urls import path
from .controllers import food

urlpatterns = [
    path('hello', food.hello),
]
