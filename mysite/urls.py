from django.contrib import admin
from main.api_views import hello_api
from django.urls import path, include  # ⬅ добавили include

urlpatterns = [
    path('api/hello/', hello_api),
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # ⬅ подключили маршруты из приложения
]