from django.forms import model_to_dict
from django.shortcuts import get_object_or_404

from domain.helpers import formata_preco_em_centavos
from domain.models import Produto, Parceiro
from medmais import settings


class ProdutoSessao(object):

    def __init__(self, request):
        self.session = request.session
        self.produtos = self.session.get(settings.PRODUTOS_SESSION_ID)

        if not self.produtos:
            self.produtos = self.session[settings.PRODUTOS_SESSION_ID] = {}

    # { '1' : { 'id': '1', 'preco': '700', 'quantidade': 10 ... }}
    def atualiza(self, id, quantidade):
        produto = Produto.objects.get(id=id)
        id = str(id)
        if id not in self.produtos:
            self.produtos[id] = {
                'id': id,
                'preco': produto.preco,
                'quantidade': quantidade,
                'preco_total': produto.preco * quantidade,
            }
        else:
            self.produtos[id]['quantidade'] = quantidade
            self.produtos[id]['preco_total'] = self.produtos[id]['quantidade'] * self.produtos[id]['preco']

        self.salvar()

        produto_response = model_to_dict(produto)
        produto_response['parceiro'] = model_to_dict(produto.parceiro)
        return {
            **self.produtos[id],
            'data': produto_response,
        }

    def salvar(self):
        self.session.modified = True

    def remover(self, id):
        id = str(id)
        if id in self.produtos:
            del self.produtos[id]
            self.salvar()

    def get_preco_total(self, id):
        return self.produtos[id]['preco_total']

    def get_quantidade_total(self, id):
        id = str(id)
        if id in self.produtos:
            return self.produtos[id]['quantidade']
        else:
            return 0

    def get_preco_produtos(self):
        return sum(item['preco_total'] for item in self.produtos.values())

    def get_quantidade_produtos(self):
        return sum(item['quantidade'] for item in self.produtos.values())

    def get_produtos(self):
        lista = []

        if not bool(self.produtos.values()):
            return lista

        for produto_da_sessao in self.produtos.values():
            produto = Produto.objects.get(id=produto_da_sessao['id'])

            lista.append({
                'produto': produto,
                'id': produto_da_sessao['id'],
                'preco': produto_da_sessao['preco'],
                'preco_formatado': formata_preco_em_centavos(produto_da_sessao['preco']),
                'quantidade': produto_da_sessao['quantidade'],
                'preco_total': produto_da_sessao['preco_total'],
                'preco_total_formatado': formata_preco_em_centavos(produto_da_sessao['preco_total'])
            })

        return lista
