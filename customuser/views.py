from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class CreateUserView(generics.CreateAPIView):
    model = CustomUser
    permission_classes = [AllowAny]
    serializer_class = CustomUserSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def verify_token(request):
    return Response({"message": "Token is valid"}, status=200)
