# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from casadopia.models import Endereco, Habitacao, Familia, Atendido, Escolaridade, Familiar, GrauParentesco, HistoricoSaude, InstituicaoExterna

from django.contrib import admin

admin.site.register(InstituicaoExterna)
admin.site.register(Familia)
admin.site.register(Endereco)
admin.site.register(Habitacao)
admin.site.register(Familiar)
admin.site.register(Atendido)
admin.site.register(Escolaridade)
admin.site.register(HistoricoSaude)
admin.site.register(GrauParentesco)


