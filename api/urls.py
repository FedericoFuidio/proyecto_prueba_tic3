from django.urls import path
from .views import VehiculoView, api_home, main, UserView, VendedorView, CompradorView, LikeView, DislikeView, ChatView, MensajeView

urlpatterns = [
    path('home', api_home),
    path('user', UserView.as_view()),
    path('vendedor', VendedorView.as_view()),
    path('comprador', CompradorView.as_view()),
    path('vehiculo', VehiculoView.as_view()),
    path('like', LikeView.as_view()),
    path('dislike', DislikeView.as_view()),
    path('chat', ChatView.as_view()),
    path('mensaje', MensajeView.as_view())
]