"""Views module."""
from django.core.exceptions import ValidationError
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from dependency_injector.wiring import inject, Provide
from django.template.defaultfilters import slugify

from domain.models import Produto
from medmais.containers import Container
from application.forms import ProdutoForm, QuantidadeDeProdutoForm

from medmais.containers import ServicoRepository
from medmais.containers import ObjetivosRepository
from presentation.ProdutoSessao import ProdutoSessao


@inject
def index(request: HttpRequest,
          id: int = None,
          quantidade: int = None,
          servico_repository: ServicoRepository = Provide[Container.servico_repository],
          objetivos_repository: ObjetivosRepository = Provide[Container.objetivos_repository]) -> HttpResponse:

    sessao = ProdutoSessao(request)

    if request.method == 'POST' and id is None and quantidade is None:
        return cadastra_produto(request, sessao)
    elif request.method == 'POST' and id is not None and quantidade is None:
        return deleta_produto(id, sessao)
    elif request.method == 'POST' and id is not None and quantidade is not None:
        return atualiza_produto(request, sessao)

    lista_de_forms = []
    produtos = sessao.get_produtos()
    for produto in produtos:
        lista_de_forms.append(QuantidadeDeProdutoForm(
            initial={
                "quantidade": produto['quantidade'],
                "produto_id": produto['id']
            }))

    return render(
        request,
        template_name="produtos.html",
        context={
            "produtos": zip(produtos, lista_de_forms),
            "form": ProdutoForm(),
            "servicos": servico_repository.GetAll(),
            "objetivos": objetivos_repository.GetAll()
        }
    )


def cadastra_produto(request: HttpRequest, sessao: ProdutoSessao):
    form = ProdutoForm(request.POST)
    if form.is_valid():
        quantidade = form.cleaned_data['quantidade']
        produto = form.save(commit=False)
        produto.slug = slugify(produto.nome)
        produto.save()
        produto_response = sessao.atualiza(produto.id, quantidade)
    else:
        raise ValidationError('Ocorreu um erro de validacao')

    response = {
        'produto': produto_response,
        'quantidade_total': sessao.get_quantidade_produtos(),
        'preco_total': sessao.get_preco_produtos()
    }

    return JsonResponse(response)


def deleta_produto(id: int, sessao: ProdutoSessao):
    produto = get_object_or_404(Produto, pk=id)
    sessao.remover(id)
    produto.delete()

    response = {
        'id': id,
        'quantidade_total': sessao.get_quantidade_produtos(),
        'preco_total': sessao.get_preco_produtos()
    }

    return JsonResponse(response)


def atualiza_produto(request: HttpRequest, sessao: ProdutoSessao):
    form = QuantidadeDeProdutoForm(request.POST)
    if form.is_valid():
        quantidade = form.cleaned_data['quantidade']
        produto = get_object_or_404(Produto, pk=form.cleaned_data['produto_id'])
        produto_response = sessao.atualiza(produto.id, quantidade)
    else:
        raise ValidationError('Ocorreu um erro de validacao')

    response = {
        'produto': produto_response,
        'quantidade_total': sessao.get_quantidade_produtos(),
        'preco_total': sessao.get_preco_produtos()
    }
    return JsonResponse(response)
