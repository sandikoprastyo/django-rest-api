from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, pagination
from .serializers import UserSerializer

User = get_user_model()

class UsersPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 20

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = UsersPagination
    permission_classes = [permissions.IsAuthenticated]  # Hanya pengguna terotentikasi yang bisa mengakses endpoint ini
