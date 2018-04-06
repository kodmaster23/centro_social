from rest_framework import serializers

from models import Endereco, InstituicaoExterna, Familia, Habitacao, Familiar, Atendido, GrauParentesco, Escolaridade, \
    HistoricoSaude


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ('cep', 'tipo_logradouro', 'logradouro', 'numero', 'complemento', 'bairro', 'cidade')

class InstituicaoExternaSerializer(serializers.ModelSerializer):
    endereco = serializers.PrimaryKeyRelatedField(queryset=Endereco.objects.all())
    class Meta:
        model = InstituicaoExterna
        fields = ('id', 'nome', 'endereco')

class FamiliaSerializer(serializers.ModelSerializer):
    auxilio_externo = serializers.PrimaryKeyRelatedField(queryset=InstituicaoExterna.objects.all())
    class Meta:
        model = Familia
        fields = ('id', 'nis_familiar', 'cras_referencia', 'bolsa_familia', 'auxilio_externo')

class HabitacaoSerializer(serializers.ModelSerializer):
    endereco = serializers.PrimaryKeyRelatedField(queryset=Endereco.objects.all())
    familia = FamiliaSerializer(read_only=True)
    familia_id = serializers.PrimaryKeyRelatedField(queryset=Familia.objects.all(), write_only=True, source='familia')
    class Meta:
        model = Habitacao
        fields = ('id', 'tipo_domicilio', 'tipo_propriedade', 'tipo_edificacao', 'nro_comodos', 'nro_dormitorios', 'agua_encanada', 'luz_eletrica', 'gas_encanado', 'rede_esgoto', 'endereco', 'familia', 'familia_id')

class FamiliarSerializer(serializers.ModelSerializer):
    endereco = serializers.PrimaryKeyRelatedField(queryset=Endereco.objects.all())
    familia = serializers.PrimaryKeyRelatedField(queryset=Familia.objects.all())
    class Meta:
        model = Familiar
        fields = ('id', 'nome', 'sobrenome', 'cpf', 'idade', 'estado_civil', 'escolaridade', 'genero', 'profissao', 'renda_mensal', 'endereco', 'familia')

class AtendidoSerializer(serializers.ModelSerializer):
    encaminhamento = serializers.PrimaryKeyRelatedField(queryset=InstituicaoExterna.objects.all())
    familia = serializers.PrimaryKeyRelatedField(queryset=Familia.objects.all())
    class Meta:
        model = Atendido
        fields = ('id','nome', 'sobrenome', 'cpf', 'rg', 'data_nascimento', 'telefone_primario', 'telefone_secundario', 'genero', 'turno', 'encaminhamento', 'familia')

class GrauParentescoSerializer(serializers.ModelSerializer):
    atendido = serializers.PrimaryKeyRelatedField(queryset=Atendido.objects.all())
    familiar = serializers.PrimaryKeyRelatedField(queryset=Familiar.objects.all())
    class Meta:
        model = GrauParentesco
        fields = ('id','responsavel_legal', 'contato', 'grau', 'atendido', 'familiar')

class EscolaridadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escolaridade
        fields = '__all__'

class HistoricoSaudeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricoSaude
        fields = '__all__'
