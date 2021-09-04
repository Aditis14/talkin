from rest_framework import serializers
from .models import *

class SubscribeSerializer(serializers.Serializer):
    email = serializers.EmailField()