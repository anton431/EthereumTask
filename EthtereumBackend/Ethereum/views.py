from django.shortcuts import render
from rest_framework import generics
from .models import Token
from .serializers import TokenSerializer,TokenSerializerSupply


class EthereumCreate(generics.CreateAPIView):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer

class EthereumViewList(generics.ListAPIView):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer

class EthereumOnlineToken(generics.ListAPIView):
    queryset = Token.objects.all()
    serializer_class = TokenSerializerSupply