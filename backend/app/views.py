from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from .models import product
from .serializers import productSerializer,userSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
def home(request):
    return HttpResponse('hello there everything is working fine')

class productsView(generics.ListCreateAPIView):
    queryset=product.objects.all()
    serializer_class=productSerializer

class userView(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=userSerializer
