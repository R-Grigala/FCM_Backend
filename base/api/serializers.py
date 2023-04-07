from rest_framework import serializers
from ..models import FCMToken

class TokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = FCMToken
        fields = "__all__"