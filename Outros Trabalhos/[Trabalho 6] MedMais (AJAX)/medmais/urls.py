"""medmais URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from presentation.views import home_views, sobre_views, contato_views, servico_views, parceiros_views, produtos_views

urlpatterns = [
    path('', home_views.index, name='home'),
    path('sobre/', sobre_views.index, name='sobre'),
    path('contato/', contato_views.index, name='contato'),
    path('servicos/', servico_views.index, name='servico'),
    path('cadastro-de-parceiros/', parceiros_views.cadastra_parceiro, name='cadastro-de-parceiros'),
    path('parceiros/', parceiros_views.index, name='parceiros'),
    path('parceiros/<int:id>', parceiros_views.exibe, name='parceiros-exibe'),
    path('parceiros/editar/<int:id>', parceiros_views.edita, name='parceiros-edita'),
    path('parceiros/deletar/<int:id>', parceiros_views.deleta, name='parceiros-deleta'),
    path('produtos/<int:id>/quantidade/<int:quantidade>', produtos_views.index, name='produtos'),
    path('produtos/<int:id>', produtos_views.index, name='produtos'),
    path('produtos/', produtos_views.index, name='produtos'),
    path('admin/', admin.site.urls),
]
