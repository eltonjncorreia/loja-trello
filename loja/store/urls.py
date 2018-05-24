from django.urls import path
from loja.store.views import home, carrinho

app_name = "store"
urlpatterns = [
    path('', home, name="home"),
    path('carrinho/<uuid:pk>/', carrinho, name="carrinho"),
]