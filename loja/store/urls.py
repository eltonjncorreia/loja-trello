from django.urls import path
from loja.store.views import home, carrinho, remove, cartao_trello, pedidos

app_name = "store"
urlpatterns = [
    path('', home, name="home"),
    path('pedidos/', pedidos, name="pedidos"),
    path('carrinho/<uuid:pk>/', carrinho, name="carrinho"),
    path('remove/<uuid:pk>/', remove, name="remove"),
    path('trello/', cartao_trello, name="trello"),
]
