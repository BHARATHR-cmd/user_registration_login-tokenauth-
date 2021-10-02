from django.urls import path, re_path
from .views import UserAPIView,  ProductsList
# from .views import obtain_auth_token


urlpatterns = [
    path('', UserAPIView.as_view()),

    path('<str:pk>/', UserAPIView.as_view()),  # to capture our ids
    path('products', ProductsList.as_view(), name="products"),
    # re_path(r'^api-token-auth/', obtain_auth_token),
]
