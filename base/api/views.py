from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.contrib.auth.decorators import login_required
# from rest_framework.decorators import api_view
from ..models import FCMToken
from .serializers import TokenSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


# @csrf_exempt
# @login_required
# def save_fcm_token(request):
#     if request.method == 'POST':
#         fcm_token, created = FCMToken.objects.get_or_create(user=request.user)
#         fcm_token.token = request.POST.get('token')
#         fcm_token.save()
#         return JsonResponse({'success': True})
#     else:
#         return JsonResponse({'success': False, 'error': 'Invalid method'})
    
# @api_view(['GET'])
# def token_list(request, format=None):

#     if request.method == 'GET':
#         events = FCMToken.objects.all()
#         serializer = TokenSerializer(events, many=True)
#         return Response(serializer.data)

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class ExampleView(APIView):
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