from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import todo
from todo import serializers

class todoListviews(generics.ListAPIView):
    queryset = todo.objects.all()
    serializer_class = serializers.todofewserilizers

class todocreateview(generics.CreateAPIView):
    queryset = todo.objects.all()
    serializer_class = serializers.todofewserilizers

class AdmintodoListCreateview(generics.ListCreateAPIView):
    queryset = todo.objects.all()
    serializer_class = serializers.todofewserilizers
