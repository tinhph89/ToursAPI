from django.shortcuts import render
from rest_framework import viewsets
from .models import Tours
from .serializers import TourSerializer
# Create your views here.

class ToursViewSet(viewsets.ModelViewSet):
    queryset = Tours.objects.all()
    serializer_class = TourSerializer
