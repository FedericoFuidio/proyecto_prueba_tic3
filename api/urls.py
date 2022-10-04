from django.urls import path
from .views import main, RoomView, PersonView, UserView, VendedorView

urlpatterns = [
    path('home', main),
    path('room', RoomView.as_view()),
    path('person', PersonView.as_view()),
    path('user', UserView.as_view()),
    path('vendedor', VendedorView.as_view())
]