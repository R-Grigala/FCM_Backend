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


class ExampleView(APIView):

    def get(self, request, format=None):
        events = FCMToken.objects.all()
        serializer = TokenSerializer(events, many=True)
        return Response(serializer.data)
