from domain.models import Cliente

class ClienteRepository:

    def GetAll(self) -> list[Cliente]:
        return Cliente.objects.all().order_by("nome")
