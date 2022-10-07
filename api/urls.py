from django.urls import path
from .views import api_home, main, UserView, VendedorView

urlpatterns = [
    path('home', api_home),
    path('user', UserView.as_view()),
    path('vendedor', VendedorView.as_view())
]