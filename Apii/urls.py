from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
# from rest_framework.authtoken.serializers import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('registration.urls')),
    path('api/token/', obtain_auth_token, name='obtain-token')
]
