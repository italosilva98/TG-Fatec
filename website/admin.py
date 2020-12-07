from django.contrib import admin
from .models import Service, PaginaIndex, Contato

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(PaginaIndex)
class PaginaIndexAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('email','telefone1','telefone2',    )
    
    fieldsets = (
        (None, {
            'fields': (
                ('telefone1','telefone2'),('email','skype'),'endereco',
            )
        }),
    )
