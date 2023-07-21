from django.shortcuts import render
from rest_framework import viewsets, mixins
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.response import Response

class TodoViewSet(viewsets.ModelViewSet, mixins.CreateModelMixin):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = TodoSerializer(queryset, many=True)
        return Response({"data": serializer.data})