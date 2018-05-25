from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url as r

from loja.api.models import Produto, Pedido


def home(request):
    produtos = Produto.objects.all()
    pedidos = produtos.filter(produtos_em_pedidos__us=request.user)
    return render(request, 'store/home.html', {'produtos': produtos, 'pedidos': pedidos})


def carrinho(request, pk=None):
    try:
        produto = Produto.objects.get(pk=pk)
        pedido = Pedido(us=request.user)
        if not Pedido.objects.filter(us=request.user):
            pedido.save()

        pedido = Pedido.objects.get(us__exact=request.user)
        pedido.produto.add(produto)
        pedido.preco += pedido.produto.preco
        pedido.save(force_update=True)

    except Produto.DoesNotExist:
        raise ValueError('Error')

    return HttpResponseRedirect(r('store:home'))


def checkout(request):
    pass

