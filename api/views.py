from django.shortcuts import render
from django.http import JsonResponse
from api.models import Sneaker

# Create your views here.
def get_sneakers(request):
    sneakers = Sneaker.objects.all()
    sneakers_python = list(sneakers.values())
    return JsonResponse(
        {
        'sneakers': sneakers_python
        }
    )
