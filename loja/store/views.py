from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url as r

from loja.api.serializers import PedidoSerializer
from loja.settings import API_KEY, API_TOKEN
from loja.api.models import Produto, Pedido

from trello import TrelloClient
from uuid import UUID
import json


def home(request):
    produtos = Produto.objects.all()
    pedidos = produtos.filter(produtos_em_pedidos__us=request.user)

    pedido = pedidos.only('id').latest('id')
    cartao_trello(request, pedido=pedido.pk, desc=pedido.nome)

    return render(request, 'store/home.html', {'produtos': produtos, 'pedidos': pedidos})


def carrinho(request, pk=None):
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
    try:
        pedido = Pedido.objects.filter(us__exact=request.user).get(produto__id__exact=pk)
        pedido.produto.remove(pk)

    except Pedido.DoesNotExist:
        raise ValueError('Erro')

    return HttpResponseRedirect(r('store:home'))


def cartao_trello(request, pedido=None, desc=None):
    cliente = TrelloClient(api_key=API_KEY, api_secret=API_TOKEN)
    my_boards = cliente.get_board('hmetG8k4')
    lista = my_boards.all_lists()

    pedido = json.dumps(pedido, cls=UUIDEncoder)
    lista[0].add_card(name=pedido, desc=desc, position=0)

    return HttpResponseRedirect(r('store:home'))


class UUIDEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            # if the obj is uuid, we simply return the value of uuid
            return obj.hex
        return json.JSONEncoder.default(self, obj)
