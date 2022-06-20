"""Views module."""
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from dependency_injector.wiring import inject, Provide

from medmais.containers import Container

from medmais.containers import ServicoRepository
from medmais.containers import ObjetivosRepository
from medmais.containers import ContatoRepository

@inject
def index(request: HttpRequest,
          servico_repository: ServicoRepository = Provide[Container.servico_repository],
          objetivos_repository: ObjetivosRepository = Provide[Container.objetivos_repository],
          contato_repository: ContatoRepository = Provide[Container.contato_repository]) -> HttpResponse:

    return render(
        request,
        template_name="contato.html",
        context={
            'cards': contato_repository.GetAll(),
            "servicos": servico_repository.GetAll(),
            "objetivos": objetivos_repository.GetAll()
        }
    )
