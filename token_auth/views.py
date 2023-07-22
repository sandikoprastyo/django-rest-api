from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from .serializers import TokenSerializer

class ObtainAuthToken(APIView):
    def post(self, request):
        token, created = Token.objects.get_or_create(user=request.user)
        return Response({'token': token.key})

class GetAuthToken(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            token = Token.objects.get(user=request.user)
            serializer = TokenSerializer(token)
            return Response(serializer.data)
        except Token.DoesNotExist:
            return Response({'error': 'Token not found for this user.'}, status=404)
