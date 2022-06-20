from dependency_injector.wiring import inject, Provide

from medmais.containers import ClienteRepository

class ClienteService:
    @inject
    def __init__(self, cliente_repository: ClienteRepository = Provide[ClienteRepository]):
        self._cliente_repository = cliente_repository

    def ObterTodos(self):
        return self._cliente_repository.GetAll()
