from django.urls import path
from .views import UserAPIView,  ProductsList


urlpatterns = [
    path('', UserAPIView.as_view()),

    path('<str:pk>/', UserAPIView.as_view()),  # to capture our ids
    path('products', ProductsList.as_view(), name="products"),
]
