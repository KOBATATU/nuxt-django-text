from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from app.serializer import InputTextSerializer
from .models import InputText

class PredictAPIView(generics.GenericAPIView):
    serializer_class = InputTextSerializer

    def post(self,request):
        # これでInputTextのgetメソッドが呼び出される．
        serializer = self.get_serializer(request.data)
        return Response(serializer.data,status = status.HTTP_200_OK)