from rest_framework.viewsets import ModelViewSet
from .models import Pedido, Produto, Categoria, Estoque
from .serializers import ProdutoSerializer, CategoriaSerializer, \
                         PeditoSerializer, EstoqueSerializer


class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class PedidoViewSet(ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PeditoSerializer


class EstoqueViewSet(ModelViewSet):
    queryset = Estoque.objects.all()
    serializer_class = EstoqueSerializer

