from django.urls import path
from .controllers import tourism

urlpatterns = [
    path('hello', tourism.hello),
    path('predict', tourism.predict),
    path('multi-predict', tourism.multi_predict),
]
