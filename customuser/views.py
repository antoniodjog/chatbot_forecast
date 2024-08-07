from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import CustomUser
from .serializers import CustomUserSerializer

class CreateUserView(generics.CreateAPIView):
    model = CustomUser
    permission_classes = [AllowAny]
    serializer_class = CustomUserSerializer

