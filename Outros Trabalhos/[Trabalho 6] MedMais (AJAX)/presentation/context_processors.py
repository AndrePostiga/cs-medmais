import locale

from domain.helpers import formata_preco_em_centavos
from presentation.ProdutoSessao import ProdutoSessao


def calcula_totais_produtos(request):
    produtos = ProdutoSessao(request)
    quantidade = produtos.get_quantidade_produtos()
    preco = formata_preco_em_centavos(produtos.get_preco_produtos())

    return {
        'quantidade': quantidade,
        'preco': preco
    }