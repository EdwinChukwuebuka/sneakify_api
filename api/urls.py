from django.urls import path
from api.views import get_sneakers, sneaker_create

urlpatterns = [
    path('', sneaker_create),
    path('sneakers/', get_sneakers)
]