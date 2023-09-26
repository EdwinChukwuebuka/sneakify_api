from django.urls import path
from api.views import get_sneakers

urlpatterns = [
    path('sneakers/', get_sneakers)
]