from django.urls import path
from loja.store.views import home, carrinho, remove

app_name = "store"
urlpatterns = [
    path('', home, name="home"),
    path('carrinho/<uuid:pk>/', carrinho, name="carrinho"),
    path('remove/<uuid:pk>/', remove, name="remove"),
]