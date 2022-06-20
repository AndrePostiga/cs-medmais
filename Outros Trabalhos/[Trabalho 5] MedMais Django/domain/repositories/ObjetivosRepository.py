from domain.models import Objetivo

class ObjetivosRepository:

    def GetAll(self) -> list[Objetivo]:
        return Objetivo.objects.all()
