from django.urls import path
from .views import ProductAPIView, ProductAPIView2
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('product/', ProductAPIView.as_view()),
    path('product/<int:pk>/', ProductAPIView2.as_view()),
   
]
urlpatterns = format_suffix_patterns(urlpatterns)