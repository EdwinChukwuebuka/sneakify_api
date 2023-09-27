from django.shortcuts import render
from django.http import JsonResponse
from api.models import Sneaker
from .serializer import SneakerSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def get_sneakers(request):
    sneakers = Sneaker.objects.all()
    serializer = SneakerSerializer(sneakers, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def sneaker_create(request):
    serializer = SneakerSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

