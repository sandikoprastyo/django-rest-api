from rest_framework import viewsets, mixins, pagination
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class TodoPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 20


class TodoListCreateView(viewsets.ModelViewSet, mixins.CreateModelMixin):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    pagination_class = TodoPagination

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)


        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        # else return
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)