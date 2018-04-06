from rest_framework import viewsets, pagination

from casadopia.models import Endereco, InstituicaoExterna, Familia, Habitacao, Familiar, Atendido, GrauParentesco, \
    Escolaridade, HistoricoSaude
from casadopia.serializers import EnderecoSerializer, InstituicaoExternaSerializer, FamiliaSerializer, \
    HabitacaoSerializer, FamiliarSerializer, AtendidoSerializer, GrauParentescoSerializer, EscolaridadeSerializer, \
    HistoricoSaudeSerializer

class MyPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_description = 'page_size'
    max_page_size = 30

class EnderecoViewSet(viewsets.ModelViewSet):
    serializer_class = EnderecoSerializer
    queryset = Endereco.objects.all()
    pagination_class = MyPagination

class InstituicaoExternaViewSet(viewsets.ModelViewSet):
    serializer_class = InstituicaoExternaSerializer
    queryset = InstituicaoExterna.objects.all()
    pagination_class = MyPagination

class FamiliaViewSet(viewsets.ModelViewSet):
    serializer_class = FamiliaSerializer
    queryset = Familia.objects.all()
    pagination_class = MyPagination

class HabitacaoViewSet(viewsets.ModelViewSet):
    serializer_class = HabitacaoSerializer
    queryset = Habitacao.objects.all()
    pagination_class = MyPagination

class FamiliarViewSet(viewsets.ModelViewSet):
    serializer_class = FamiliarSerializer
    queryset = Familiar.objects.all()
    pagination_class = MyPagination

class AtendidoViewSet(viewsets.ModelViewSet):
    serializer_class = AtendidoSerializer
    queryset = Atendido.objects.all()
    pagination_class = MyPagination

class GrauParentescoViewSet(viewsets.ModelViewSet):
    serializer_class = GrauParentescoSerializer
    queryset = GrauParentesco.objects.all()
    pagination_class = MyPagination

class EscolaridadeViewSet(viewsets.ModelViewSet):
    serializer_class = EscolaridadeSerializer
    queryset = Escolaridade.objects.all()
    pagination_class = MyPagination

class HistoricoSaudeViewSet(viewsets.ModelViewSet):
    serializer_class = HistoricoSaudeSerializer
    queryset = HistoricoSaude.objects.all()
    pagination_class = MyPagination
