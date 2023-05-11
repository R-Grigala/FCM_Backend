from ..models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class FCMView(APIView):
    # Require authentication and authorization for this endpoint
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Retrieve all FCMToken objects from the database
        tokens = FCMToken.objects.all()

        # Serialize the FCMToken objects
        serializer = TokenSerializer(tokens, many=True)

        # Return the serialized data
        return Response(serializer.data)

    def post(self, request):
        # Extract the token value from the request body
        token = request.data.get('token')

        # Check if a token with the same value already exists
        existing_token = FCMToken.objects.filter(token=token).first()

        if existing_token:
            # If a token with the same value exists, update its updated_at field
            existing_token.save()

            # Serialize the updated FCMToken object
            serializer = TokenSerializer(existing_token)
        else:
            # If a token with the same value does not exist, create a new FCMToken object with the provided token value
            token_object = FCMToken.objects.create(token=token)

            # Serialize the new FCMToken object
            serializer = TokenSerializer(token_object)

        # Return the serialized data
        return Response(serializer.data)
    

class NewsView(APIView):
    # Require authentication and authorization for this endpoint
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self, request):
        # Retrieve all FCMToken objects from the database
        news = NewsPost.objects.all()

        # Serialize the FCMToken objects
        serializer = NewsSerializer(news, many=True)

        # Return the serialized data
        return Response(serializer.data)

