from datetime import date

from dependency_injector.wiring import inject, Provide

from domain.models import Parceiro
from medmais.containers import ParceiroRepository

class ParceiroService:
    @inject
    def __init__(self, parceiro_repository: ParceiroRepository = Provide[ParceiroRepository]):
        self._parceiro_repository = parceiro_repository

    def ObterTodos(self):
        return self._parceiro_repository.GetAll()

    def ObterPaginado(self, pagina, nome):
        return self._parceiro_repository.GetPagina(pagina, nome)

    def UpsertParceiro(self, parceiro: Parceiro):
        if parceiro.data_cadastro is None:
            parceiro.data_cadastro = date.today()

        parceiro.data_atualizacao = date.today()
        self._parceiro_repository.Salva(parceiro)

    def ObterPeloId(self, id: int):
        return self._parceiro_repository.GetPeloId(id)

    def DeletarPeloId(self, id: int):
        return self._parceiro_repository.Remove(id)