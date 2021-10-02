from django.contrib import admin
from django.urls import path, include, re_path
# from rest_framework.authtoken.views import obtain_auth_token
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )
# from registration.views import UserAPIView
# from rest_framework.routers import DefaultRouter
# from rest_framework.authtoken.serializers import obtain_auth_token
from registration.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('registration.urls')),
    # path('api/token/', obtain_auth_token, name='obtain-token'),
    re_path(r'^api-token-auth/', obtain_auth_token),
]
