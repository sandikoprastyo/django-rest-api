from django.urls import path
from .views import ObtainAuthToken, GetAuthToken

urlpatterns = [
    path('get-auth-token/', ObtainAuthToken.as_view(), name='get-auth-token'),
    path('get-user-token/', GetAuthToken.as_view(), name='get-user-token'),
]
