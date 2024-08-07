from django.urls import path
from .views import CreateUserView
from .views import verify_token

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register'),
    path('verify-token', verify_token, name='verify_token'),
]
