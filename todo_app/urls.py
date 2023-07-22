from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoListCreateView

router = DefaultRouter()
router.register(r'todos', TodoListCreateView)

urlpatterns = [
    path('', include(router.urls)),
]
