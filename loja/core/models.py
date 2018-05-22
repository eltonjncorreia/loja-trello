from django.db import models
import uuid


class Produto(models.Model):
    identificado = models.UUIDField(editable=False, default=uuid.uuid4())
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, related_name='categorias_produto')

    def __str__(self):
        return f'{self.nome}, {self.descricao}'


class Pedido(models.Model):
    identificado = models.UUIDField(editable=False, default=uuid.uuid4())
    produtos = models.ManyToManyField('Produto', related_name='produtos_pedidos')
    preco = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    STATUS = (('PR', 'Pedido Realizado'),
              ('SP', 'Separação em estoque'),
              ('EM', 'Em montagem'),
              ('RT', 'Realização de testes'),
              ('CO', 'Concluido'))

    status = models.CharField(max_length=2, choices=STATUS)

    def __str__(self):
        return f'{self.produtos}'


class Categoria(models.Model):
    identificado = models.UUIDField(editable=False, default=uuid.uuid4())
    nome = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.nome}'


class Estoque(models.Model):
    item = models.ForeignKey('Produto',
                             on_delete=models.CASCADE,
                             related_name='item_em_estoque')

    quantidade = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.item}, {self.quantidade}'
