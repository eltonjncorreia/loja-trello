from rest_framework import serializers

from .models import Produto, Pedido, Categoria, Estoque


class ProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produto
        fields = '__all__'


class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = '__all__'


class PeditoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pedido
        fields = '__all__'


class EstoqueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Estoque
        fields = '__all__'
