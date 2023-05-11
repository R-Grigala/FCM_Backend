from rest_framework import serializers
from ..models import *

class TokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = FCMToken
        fields = "__all__"

class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewsPost
        fields = "__all__"