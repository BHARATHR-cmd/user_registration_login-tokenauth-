from django.http.response import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from .models import CustomUser, Products
from .serializers import UserSerializers, ProductSerializer
# , AuthCustomTokenSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# from rest_framework import parsers, renderers
#
# from rest_framework import parsers, renderers
# from rest_framework.authtoken.models import Token
# from rest_framework.authtoken.serializers import AuthTokenSerializer
# from rest_framework.compat import coreapi, coreschema
# from rest_framework.response import Response
# from rest_framework.schemas import ManualSchema
# from rest_framework.schemas import coreapi as coreapi_schema
# from rest_framework.views import APIView


# class ObtainAuthToken(APIView):
#     throttle_classes = ()
#     permission_classes = ()
#     parser_classes = (
#         parsers.FormParser,
#         parsers.MultiPartParser,
#         parsers.JSONParser,
#     )

#     renderer_classes = (renderers.JSONRenderer,)

#     def post(self, request):
#         serializer = AuthCustomTokenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)

#         content = {
#             'token': unicode(token.key),
#         }

#         return Response(content)

from rest_framework.authtoken import views as auth_views
from rest_framework.compat import coreapi, coreschema
from rest_framework.schemas import ManualSchema

from .serializers import MyAuthTokenSerializer


class MyAuthToken(auth_views.ObtainAuthToken):
    serializer_class = MyAuthTokenSerializer
    if coreapi is not None and coreschema is not None:
        schema = ManualSchema(
            fields=[
                coreapi.Field(
                    name="email",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Email",
                        description="Valid email for authentication",
                    ),
                ),
                coreapi.Field(
                    name="password",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Password",
                        description="Valid password for authentication",
                    ),
                ),
            ],
            encoding="application/json",
        )


obtain_auth_token = MyAuthToken.as_view()


class UserAPIView(APIView):
    # permission_classes = (IsAuthenticated, )

    # READ a single CustomUser
    def post(self, request, format=None):
        data = request.data
        serializer = UserSerializers(data=data)

        serializer.is_valid(raise_exception=True)
        # serializer.validated_data

        serializer.save()

        response = Response()

        response.data = {
            'message': 'CustomUser Created Successfully',
            'data': serializer.data
        }

        return response

    def get_object(self, pk):
        try:
            return CustomUser.objects.filter(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
        else:
            data = CustomUser.objects.all()

        serializer = UserSerializers(data, many=True)

        return Response(serializer.data)

    def put(self, request, pk=None, format=None):
        User_to_update = CustomUser.objects.get(pk=pk)
        serializer = UserSerializers(
            instance=User_to_update, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': 'CustomUser Updated Successfully',
            'data': serializer.data
        }

        return response

    def delete(self, request, pk, format=None):
        User_to_delete = CustomUser.objects.get(pk=pk)

        User_to_delete.delete()

        return Response({
            'message': 'CustomUser Deleted Successfully'
        })


class ProductsList(APIView):
    permission_classes = (IsAuthenticated, )
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
        else:
            data = Products.objects.all()

        serializer = ProductSerializer(data, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = ProductSerializer(data=data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = Response()

        response.data = {
            'message': 'Product Created Successfully',
            'data': serializer.data
        }

        return response
