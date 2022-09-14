from django.urls import path
from .views import main, RoomView

urlpatterns = [
    path('home', main),
    path('room', RoomView.as_view())
]