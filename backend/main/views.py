from django.db.models.fields import EmailField
from django.shortcuts import render, redirect
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
# Create your views here.


class ContactPostView(generics.GenericAPIView):
    serializer_class = SubscribeSerializer

    def post(self, request, *args, **kwargs):
        data = request.data

        try:
            email = data['email']
            s = Subscribe()
            s.email = email
            s.save()
            return Response({
                "message": True
            })
        except:
            return Response({
                "message": False
            }) 