from django.urls import path
from .views import main, RoomView, PersonView

urlpatterns = [
    path('home', main),
    path('room', RoomView.as_view()),
    path('person', PersonView.as_view())
]