from domain.models import CardContato

class ContatoRepository:

    def GetAll(self) -> list[CardContato]:
        return CardContato.objects.all()
