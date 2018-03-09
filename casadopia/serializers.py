from rest_framework import serializers

from models import Endereco, InstituicaoExterna, Familia, Habitacao, Familiar, Atendido, GrauParentesco, Escolaridade, \
    HistoricoSaude


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'

class InstituicaoExternaSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstituicaoExterna
        fields = '__all__'

class FamiliaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Familia
        fields = '__all__'

class HabitacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitacao
        fields = '__all__'

class FamiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Familiar
        fields = '__all__'

class AtendidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atendido
        fields = '__all__'

class GrauParentescoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrauParentesco
        fields = '__all__'

class EscolaridadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escolaridade
        fields = '__all__'

class HistoricoSaudeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricoSaude
        fields = '__all__'
