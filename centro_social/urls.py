"""centro_social URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from casadopia.api import EnderecoViewSet, InstituicaoExternaViewSet, FamiliaViewSet, HabitacaoViewSet, FamiliarViewSet, \
    AtendidoViewSet, GrauParentescoViewSet, EscolaridadeViewSet, HistoricoSaudeViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'enderecos', EnderecoViewSet)
router.register(r'instituicoes_externas', InstituicaoExternaViewSet)
router.register(r'familias', FamiliaViewSet)
router.register(r'habitacoes', HabitacaoViewSet)
router.register(r'familiares', FamiliarViewSet)
router.register(r'atendidos', AtendidoViewSet)
router.register(r'graus_parentesco', GrauParentescoViewSet)
router.register(r'escolaridades', EscolaridadeViewSet)
router.register(r'historicos_saude', HistoricoSaudeViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^casadopia/', include('casadopia.urls')),
    url(r'^casadopia/', include(router.urls)),
]
