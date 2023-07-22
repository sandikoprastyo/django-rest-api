from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('todo_app.urls')),
    path('api/', include('token_auth.urls')),
    path('api/', include('users.urls')),
]
