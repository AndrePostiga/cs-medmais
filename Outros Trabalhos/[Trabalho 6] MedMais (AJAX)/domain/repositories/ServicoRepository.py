from domain.models import CardServico

class ServicoRepository:

    def GetAll(self) -> list[CardServico]:
        return CardServico.objects.all()
