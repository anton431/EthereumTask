from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView

from .blockchain import mint, random_srting
from .models import Token
from .serializers import TokenSerializer,TokenSerializerSupply


class TokenCreate(APIView):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer
    def post(self,request):
        serializater = TokenSerializer(data=request.data)
        serializater.is_valid(raise_exception=True)
        media_url = request.data['media_url']
        owner = request.data['owner']
        unique_hash = random_srting()

        token = Token.objects.create(
            unique_hash=unique_hash,
            tx_hash=mint(owner, media_url,unique_hash),
            media_url=media_url,
            owner=owner
        )
        return Response({'token': TokenSerializer(token).data})



class TokenViewList(generics.ListAPIView):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer

class TokenOnlineToken(generics.ListAPIView):
    queryset = Token.objects.all()
    serializer_class = TokenSerializerSupply

