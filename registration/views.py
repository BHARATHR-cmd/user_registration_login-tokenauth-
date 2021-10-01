from django.http.response import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from .models import CustomUser, Products
from .serializers import UserSerializers, ProductSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class UserAPIView(APIView):

    # READ a single CustomUser

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

    def post(self, request, format=None):
        data = request.data
        serializer = UserSerializers(data=data)

        serializer.is_valid(raise_exception=True)

# True
        # serializer.validated_data

        serializer.save()

        response = Response()

        response.data = {
            'message': 'CustomUser Created Successfully',
            'data': serializer.data
        }

        return response

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
