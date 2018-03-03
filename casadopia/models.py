# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

    def __unicode__(self):
        return self.name

class Habitacao(models.Model):

    endereco= models.ForeignKey(
        Endereco,
        models.SET_NULL,
        blank=True,
        null=True,
    )

    DOMICILIO_CHOICES = (
        ('1','Casa'),
        ('2','Apartamento'),
        ('3','Sobrado'),
    )

    PROPRIEDADE_CHOICES = (
        ('1','Própria'),
        ('2','Alugada'),
        ('3','Emprestada'),
    )

    EFICACAO_CHOICES = (
        ('1','Alvenaria'),
        ('2','Madeira'),
        ('3','Híbrido'),
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

    class Meta:
        verbose_name = 'Habitação'
        verbose_name_plural = 'Habitações'

    def __unicode__(self):
        return self.name
