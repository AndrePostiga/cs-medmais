from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

from domain.models import Parceiro

class ParceiroRepository:
    def GetAll(self) -> list[Parceiro]:
        return Parceiro.objects.all().order_by("nome")

    def GetPagina(self, pagina, nome):
        parceiros = Parceiro.objects\
            .filter(nome__icontains=nome)\
            .order_by('nome')
        return Paginator(parceiros, 6).get_page(pagina)

    def Salva(self, parceiro: Parceiro):
        parceiro.save()

    def GetPeloId(self, id: int):
        return get_object_or_404(Parceiro, pk=id)

    def Remove(self, id:int):
        parceiro = self.GetPeloId(id)
        parceiro.delete()
