from django.contrib import admin
from .models import Cargo, Servico, Funcionario, Feature, Cliente, Profissao_Cliente


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificado')


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'icone', 'ativo', 'modificado')

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ativo', 'modificado')

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('feature', 'icone', 'ativo', 'modificado')

@admin.register(Profissao_Cliente)
class Profissao_ClienteAdmin(admin.ModelAdmin):
    list_display = ('profissao_cliente', 'ativo', 'modificado')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'profissao_cliente', 'icone', 'ativo', 'modificado')
