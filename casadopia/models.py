# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime
from django.db import models

# Create your models here.

class Endereco(models.Model):
    cep = models.IntegerField()
    tipo_logradouro = models.CharField(max_length=10)
    logradouro = models.CharField(max_length=255)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=255, blank=True, null=True)
    bairro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

    def __unicode__(self):
        return self.logradouro

class InstituicaoExterna(models.Model):

    endereco = models.ForeignKey(
        Endereco,
        models.SET_NULL,
        blank=True,
        null=True,
    )

    nome = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Instituição Externa'
        verbose_name_plural = 'Instituições Externas'

    def __unicode__(self):
        return self.nome


class Familia(models.Model):

    auxilio_externo = models.ForeignKey(
        InstituicaoExterna,
        models.SET_NULL,
        blank=True,
        null=True,
    )

    nis_familiar = models.IntegerField()
    cras_referencia = models.CharField(max_length=255, null=True, blank=True)
    bolsa_familia = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Família'
        verbose_name_plural = 'Famílias'

    def __unicode__(self):
        return str(self.nis_familiar)


class Habitacao(models.Model):

    endereco= models.ForeignKey(
        Endereco,
        models.CASCADE
    )

    familia= models.ForeignKey(
        Familia,
        models.CASCADE
    )

    DOMICILIO_CHOICES = (
        ('1','Casa'),
        ('2','Apartamento'),
        ('3','Sobrado')
    )

    PROPRIEDADE_CHOICES = (
        ('1','Própria'),
        ('2','Alugada'),
        ('3','Emprestada')
    )

    EFICACAO_CHOICES = (
        ('1','Alvenaria'),
        ('2','Madeira'),
        ('3','Híbrido')
    )

    STATUS_CHOICES = (
        ('1', 'Individual'),
        ('2', 'Coletivo'),
        ('3', 'Não tem')
    )

    tipo_domicilio = models.IntegerField(choices=DOMICILIO_CHOICES, default='1')
    tipo_propriedade = models.IntegerField(choices=PROPRIEDADE_CHOICES, default='1')
    tipo_edificacao = models.IntegerField(choices=EFICACAO_CHOICES, default='1')
    nro_comodos = models.IntegerField()
    nro_dormitorios = models.IntegerField()
    agua_encanada = models.IntegerField(choices=STATUS_CHOICES, default='1')
    luz_eletrica = models.IntegerField(choices=STATUS_CHOICES, default='1')
    gas_encanado = models.IntegerField(choices=STATUS_CHOICES, default='1')
    rede_esgoto = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Habitação'
        verbose_name_plural = 'Habitações'

    def __unicode__(self):
        return self.tipo_domicilio


class Familiar(models.Model):

    ESTADO_CIVIL_CHOICES = (
        ('1', 'Solteiro'),
        ('2', 'Casado'),
        ('3', 'União Estável'),
        ('4', 'Viúvo')
    )
    GENERO_CHOICES = (
        ('1', 'Masculino'),
        ('2', 'Feminino'),
        ('3', 'Transgênero')
    )

    ESCOLARIDADE_CHOICES = (
        ('1', 'Fundamental - Incompleto'),
        ('2', 'Fundamental - Completo'),
        ('3', 'Médio - Incompleto'),
        ('4', 'Médio - Completo'),
        ('5', 'Superior - Incompleto'),
        ('6', 'Superior - Completo'),
        ('7', 'Pós-graduação (Lato senso) - Incompleto'),
        ('8', 'Pós-graduação (Lato senso) - Completo'),
        ('9', 'Pós-graduação (Stricto sensu, nível mestrado) - Incompleto'),
        ('10', 'Pós-graduação (Stricto sensu, nível mestrado) - Completo'),
        ('11', 'Pós-graduação (Stricto sensu, nível doutor) - Incompleto'),
        ('12', 'Pós-graduação (Stricto sensu, nível doutor) - Completo')
    )

    endereco = models.ForeignKey(
        Endereco,
        models.SET_NULL,
        blank=True,
        null=True,
    )

    familia = models.ForeignKey(
        Familia,
        models.CASCADE
    )

    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    cpf = models.IntegerField(null=True, blank=True)
    idade = models.IntegerField()
    estado_civil = models.IntegerField(choices=ESTADO_CIVIL_CHOICES, null=True, blank=True)
    escolaridade = models.IntegerField(choices=ESCOLARIDADE_CHOICES)
    genero = models.IntegerField(choices=GENERO_CHOICES)
    profissao = models.CharField(max_length=255)
    renda_mensal = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Familiar'
        verbose_name_plural = 'Familiares'

    def __unicode__(self):
        return self.nome


class Atendido(models.Model):

    TURNO_CHOICES = (
        ('1', 'Matutino'),
        ('2', 'Vespertino')
    )

    familia = models.ForeignKey(
        Familia,
        models.CASCADE
    )

    GENERO_CHOICES = (
        ('1', 'Masculino'),
        ('2', 'Feminino'),
        ('3', 'Transgênero')
    )

    encaminhamento = models.ForeignKey(
        InstituicaoExterna,
        models.SET_NULL,
        blank=True,
        null=True,
    )

    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    cpf = models.IntegerField()
    rg = models.IntegerField()
    data_nascimento = models.DateField()
    telefone_primario = models.IntegerField()
    telefone_secundario = models.IntegerField()
    genero = models.IntegerField(choices=GENERO_CHOICES)
    turno = models.IntegerField(choices=TURNO_CHOICES)
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Atendido'
        verbose_name_plural = 'Atendidos'

    def __unicode__(self):
        return self.nome



class GrauParentesco(models.Model):

    GRAU_CHOICES = (
        ('1','Pai'),
        ('2','Mãe'),
        ('3', 'Padrasto'),
        ('4', 'Madrasta'),
        ('5','Irmão'),
        ('6','Avô'),
        ('7','Tio'),
        ('8','Sobrinho'),
        ('9','Bisavô'),
        ('10','Primo'),
        ('11','Cunhado')
    )

    familiar = models.ForeignKey(
        Familiar,
        models.CASCADE
    )
    atendido = models.ForeignKey(
        Atendido,
        models.CASCADE
    )
    responsavel_legal = models.BooleanField(default=False)
    contato = models.BooleanField(default=False)
    grau = models.IntegerField(choices=GRAU_CHOICES)

    class Meta:
        verbose_name = 'Grau de Parentesco'
        verbose_name_plural = 'Graus de Paretesco'

    def __unicode__(self):
        return (self.grau)


class Escolaridade(models.Model):

    TURNO_CHOICES = (
        ('1','Matutino'),
        ('2','Vespertino')
    )

    SERIE_CHOICES = (
        ('1', '1º'),
        ('2', '2º'),
        ('3', '3º'),
        ('4', '4º'),
        ('5', '5º'),
        ('6', '6º'),
        ('7', '7º'),
        ('8', '8º'),
        ('9', '9º'),
    )

    atendido = models.ForeignKey(
        Atendido,
        models.CASCADE
    )

    escola = models.ForeignKey(
        InstituicaoExterna,
        models.SET_NULL,
        blank=True,
        null=True,
    )
    turno = models.IntegerField(choices=TURNO_CHOICES)
    serie = models.IntegerField(choices=SERIE_CHOICES)

    ano = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(datetime.now().year)])

    reprovou = models.BooleanField(default=False)
    observacao = models.TextField()

    class Meta:
        verbose_name = 'Escolaridade'
        verbose_name_plural = 'Escolaridade'

    def __unicode__(self):
        return str(self.ano)


class HistoricoSaude(models.Model):

    TIPO_REGISTRO_CHOICES = (
        ('1','Diagnóstico físico'),
        ('2','Diagnóstico mental'),
        ('3','Acompanhamento profissional'),
        ('4','Uso continuo de medicamentos'),
        ('5','Alergias')
    )
    atendido = models.ForeignKey(
        Atendido,
        models.CASCADE
    )

    tipo = models.IntegerField(choices=TIPO_REGISTRO_CHOICES)
    descricao = models.TextField()

    class Meta:
        verbose_name = 'Histórico de Saúde'
        verbose_name_plural = 'Histórico de Saúde'

    def __unicode__(self):
        return str(self.tipo)
