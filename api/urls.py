from django.urls import path
from .views import api_home, main, UserView, VendedorView, CompradorView

urlpatterns = [
    path('home', api_home),
    path('user', UserView.as_view()),
    path('vendedor', VendedorView.as_view()),
    path('comprador', CompradorView.as_view())
]