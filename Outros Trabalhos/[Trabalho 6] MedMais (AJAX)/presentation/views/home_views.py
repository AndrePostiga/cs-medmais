"""Views module."""
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from dependency_injector.wiring import inject, Provide

from medmais.containers import Container
from application.Services import ClienteService

from medmais.containers import ServicoRepository
from medmais.containers import ObjetivosRepository

@inject
def index(request: HttpRequest,
          cliente_service: ClienteService = Provide[Container.cliente_service],
          servico_repository: ServicoRepository = Provide[Container.servico_repository],
          objetivos_repository: ObjetivosRepository = Provide[Container.objetivos_repository]) -> HttpResponse:

    return render(
        request,
        template_name="index.html",
        context={
            "clientes": cliente_service.ObterTodos(),
            "servicos": servico_repository.GetAll(),
            "objetivos": objetivos_repository.GetAll()
        }
    )
