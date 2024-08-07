import requests
from rest_framework import generics, permissions
from .models import Message
from .serializers import MessageSerializer

class MessageListCreate(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        content = self.request.data.get('content')

        API_URL = "https://antoniodjog-weather.hf.space/api/v1/prediction/5b434e72-a5a4-4210-b88b-4ff3e198df85"
        headers = {"Authorization": "Bearer 5EQGO2BwzeCxH8NDasEU_tH3Z-aRFabF-KoH_GxLG-w"}

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()
    
        output = query({
        "question": content,
        })
        serializer.save(user=user, response=output.get('text'))
