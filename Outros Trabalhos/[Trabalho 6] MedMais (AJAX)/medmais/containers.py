"""Containers module."""

from dependency_injector import containers, providers

from domain.repositories.ClienteRepository import ClienteRepository
from domain.repositories.ServicoRepository import ServicoRepository
from domain.repositories.ObjetivosRepository import ObjetivosRepository
from domain.repositories.ContatoRepository import ContatoRepository
from domain.repositories.ParceiroRepository import ParceiroRepository

from application.Services.ClienteService import ClienteService
from application.Services.ParceiroService import ParceiroService


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    # Repositories
    cliente_repository = providers.Factory(
        ClienteRepository
    )

    servico_repository = providers.Factory(
        ServicoRepository
    )

    objetivos_repository = providers.Factory(
        ObjetivosRepository
    )

    contato_repository = providers.Factory(
        ContatoRepository
    )

    parceiro_repository = providers.Factory(
        ParceiroRepository
    )

    # Services
    cliente_service = providers.Factory(
        ClienteService,
        cliente_repository=cliente_repository
    )

    parceiro_service = providers.Factory(
        ParceiroService,
        parceiro_repository=parceiro_repository
    )

    wiring_config = containers.WiringConfiguration(
        packages=["presentation.views", "application.Services", "domain.repositories"])
