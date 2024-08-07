from django.contrib import admin
from django.urls import path, include,re_path
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()

urlpatterns = [
     path('api/', include([
        re_path(r'^', include(router.urls)),
        path('admin/', admin.site.urls),
        path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
        path('register/', include('customuser.urls')), 
        path('', include('chatbot_app.urls')), 
    ])),

]
