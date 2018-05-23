from django.urls import path, include
from rest_framework import routers

from .views import ProdutoViewSet, PedidoViewSet, CategoriaViewSet, EstoqueViewSet

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'produtos', ProdutoViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'estoques', EstoqueViewSet)


urlpatterns = [
       path('v1/', include(router.urls)),
]