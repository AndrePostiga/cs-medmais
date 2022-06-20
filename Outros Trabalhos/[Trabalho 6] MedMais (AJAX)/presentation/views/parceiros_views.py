"""Views module."""
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from dependency_injector.wiring import inject, Provide

from medmais.containers import Container
from application.Services import ParceiroService
from application.forms import ParceirosSearchForm, ParceirosCadastroForm

from medmais.containers import ServicoRepository
from medmais.containers import ObjetivosRepository

@inject
def index(request: HttpRequest,
          parceiro_service: ParceiroService = Provide[Container.parceiro_service],
          servico_repository: ServicoRepository = Provide[Container.servico_repository],
          objetivos_repository: ObjetivosRepository = Provide[Container.objetivos_repository]) -> HttpResponse:

    pagina = request.GET.get('pagina')
    formNome = ParceirosSearchForm(request.GET)
    if formNome.is_valid():
        nome = formNome.cleaned_data['nome']
        return render(
            request,
            template_name="parceiros.html",
            context={
                "parceiros": parceiro_service.ObterPaginado(pagina, nome),
                "form": formNome,
                "nome": nome,
                "servicos": servico_repository.GetAll(),
                "objetivos": objetivos_repository.GetAll()
            }
        )
    else:
        raise ValueError('Ocorreu um erro inesperado ao tentar recuperar os dados de parceiro')

@inject
def exibe(request: HttpRequest,
          id : int,
          parceiro_service: ParceiroService = Provide[Container.parceiro_service],
          servico_repository: ServicoRepository = Provide[Container.servico_repository],
          objetivos_repository: ObjetivosRepository = Provide[Container.objetivos_repository]) -> HttpResponse:

    try:
        parceiro = parceiro_service.ObterPeloId(id)
    except:
        parceiro = None

    return render(
        request,
        template_name="parceiros.html",
        context={
            "parceiros": [parceiro] if parceiro else [],
            "servicos": servico_repository.GetAll(),
            "objetivos": objetivos_repository.GetAll()
        }
    )


@inject
def cadastra_parceiro(request: HttpRequest,
          parceiro_service: ParceiroService = Provide[Container.parceiro_service],
          servico_repository: ServicoRepository = Provide[Container.servico_repository],
          objetivos_repository: ObjetivosRepository = Provide[Container.objetivos_repository]) -> HttpResponse:

    if request.POST:
        parceiro_id = request.session.get('parceiro_id')

        if parceiro_id:
            parceiro = parceiro_service.ObterPeloId(parceiro_id)
            form = ParceirosCadastroForm(request.POST, instance=parceiro)
        else:
            form = ParceirosCadastroForm(request.POST)

        if form.is_valid():
            parceiro = form.save(commit=False)
            parceiro_service.UpsertParceiro(parceiro)

            if parceiro_id:
                messages.add_message(request, messages.INFO, 'Parceiro alterado com sucesso!')
                del request.session['parceiro_id']
            else:
                messages.add_message(request, messages.INFO, 'Parceiro cadastrado com sucesso!')

            return redirect('parceiros-exibe', id=parceiro.id)

    else:
        if 'parceiro_id' in request.session:
            del request.session['parceiro_id']

        form = ParceirosCadastroForm()

    return render(
        request,
        template_name="cadastro-parceiros.html",
        context={
            "form": form,
            "servicos": servico_repository.GetAll(),
            "objetivos": objetivos_repository.GetAll()
        }
    )

@inject
def edita(request: HttpRequest,
          id : int,
          parceiro_service: ParceiroService = Provide[Container.parceiro_service],
          servico_repository: ServicoRepository = Provide[Container.servico_repository],
          objetivos_repository: ObjetivosRepository = Provide[Container.objetivos_repository]) -> HttpResponse:

    parceiro = parceiro_service.ObterPeloId(id)
    form = ParceirosCadastroForm(instance=parceiro)
    request.session['parceiro_id'] = id

    return render(
        request,
        template_name="cadastro-parceiros.html",
        context={
            "form": form,
            "servicos": servico_repository.GetAll(),
            "objetivos": objetivos_repository.GetAll()
        }
    )

@inject
def deleta(request: HttpRequest,
          id : int,
          parceiro_service: ParceiroService = Provide[Container.parceiro_service],
          servico_repository: ServicoRepository = Provide[Container.servico_repository],
          objetivos_repository: ObjetivosRepository = Provide[Container.objetivos_repository]) -> HttpResponse:

    parceiro_service.DeletarPeloId(id)
    messages.add_message(request, messages.INFO, 'Parceiro deletado com sucesso!')
    return redirect('parceiros')