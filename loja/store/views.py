"""Responsavel por adicionar e remover produtos aos pedidos."""

from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url as r


from loja.settings import API_KEY, API_TOKEN
from loja.api.models import Produto, Pedido

from trello import TrelloClient
from uuid import UUID
import json


@login_required(login_url='/login/')
def home(request):
    """Pagina home, lista os produtos e adiciona no carrinho."""
    produtos = Produto.objects.all()
    pedidos = produtos.filter(produtos_em_pedidos__us=request.user)
    return render(request, 'store/home.html', {'produtos': produtos,
                                               'pedidos': pedidos})


def carrinho(request, pk=None):
    """Adiciona ao carrinho pedido baseado no user logado."""
    try:
        produto = Produto.objects.get(pk=pk)
        pedido = Pedido(us=request.user)
        if not Pedido.objects.filter(us=request.user):
            pedido.save()

        pedido = Pedido.objects.get(us__exact=request.user)
        pedido.produto.add(produto)
        pedido.preco += produto.preco
        pedido.save(force_update=True)

    except Produto.DoesNotExist:
        raise ValueError('Error')
    return HttpResponseRedirect(r('store:home'))


def remove(request, pk):
    """Remode produto que está em pedidos por usuario."""
    try:
        pedido = Pedido.objects.filter(produto=pk).get(us_id=request.user)
        pedido.produto.remove(pk)
    except Pedido.DoesNotExist:
        raise ValueError('Erro')

    return HttpResponseRedirect(r('store:home'))


def pedidos(request):
    """Enviar pedidos para o trello."""
    ped = Pedido.objects.filter(us_id=request.user)
    for pedido in ped.all():
        cartao_trello(request, pedido=pedido.pk, desc=pedido.produto.all())

    return HttpResponseRedirect(r('store:home'))


def cartao_trello(request, pedido=None, desc=None):
    """Responsavel por enviar ao cartao trello."""
    cliente = TrelloClient(api_key=API_KEY, api_secret=API_TOKEN)
    my_boards = cliente.get_board('kyL57xiF')
    lista = my_boards.all_lists()

    pedido = json.dumps(pedido, cls=UUIDEncoder)
    desc = serializers.serialize('json', desc)
    lista[0].add_card(name=pedido, desc=desc, position=0)

    return HttpResponseRedirect(r('store:home'))


class UUIDEncoder(json.JSONEncoder):
    """Class encode UUID."""

    def default(self, obj):
        """Usando para enviar UUID."""
        if isinstance(obj, UUID):
            return obj.hex
        return json.JSONEncoder.default(self, obj)
