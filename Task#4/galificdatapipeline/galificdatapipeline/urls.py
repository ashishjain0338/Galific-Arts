
from django.contrib import admin
from django.urls import path
from websocket import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.home),
    path('<str:room_name>/', views.room, name='room'),
]
