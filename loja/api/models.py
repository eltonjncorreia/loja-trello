from django.contrib.auth.models import User
from django.db import models
import uuid


class Produto(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True,
                          editable=False, default=uuid.uuid4)
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE,
                                  related_name='categorias_produtos')

    def __str__(self):
        return f'{self.nome}, {self.descricao}'


class Pedido(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True,
                          editable=False, default=uuid.uuid4)
    produto = models.ManyToManyField('Produto', related_name='produtos_em_pedidos')

    preco = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    STATUS = (('PR', 'Pedido Realizado'),
              ('SP', 'Separação em estoque'),
              ('EM', 'Em montagem'),
              ('RT', 'Realização de testes'),
              ('CO', 'Concluido'))

    status = models.CharField(max_length=2, choices=STATUS, default='PR')
    us = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.produto}'


class Categoria(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True,
                          editable=False, default=uuid.uuid4)
    nome = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.nome}'


class Estoque(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True,
                          editable=False, default=uuid.uuid4)
    item = models.ForeignKey('Produto', on_delete=models.CASCADE, related_name='itens')
    quantidade = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.item}, {self.quantidade}'



