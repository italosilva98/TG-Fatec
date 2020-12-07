from django.contrib import admin

from .models import Paciente, Prontuario


class ProntuarioAdminInline(admin.StackedInline):
    model = Prontuario
    extra = 0
    verbose_name = 'Data Consulta'
    verbose_name_plural = 'Histórico de Atendimentos'
    show_change_link = True
    can_delete = True

    classes = ('grp-collapse grp-closed',)
    # inline_classes = ('grp-collapse grp-closed',)


class PacienteAdmin(admin.ModelAdmin):
    inlines = (ProntuarioAdminInline,)

    list_display = ('nome', 'cpf','email', 'tel', 'estado_civil', 'created')

    fieldsets = (
        ('Informações Gerais', {
            # 'classes': ('grp-collapse grp-closed',),
            'fields': (
            ('nome', 'datanasc',), ('cpf', 'religiao'), ('estado_civil', 'profissao'), ('endereco', 'escolaridade'),
            ('email', 'tel'), 'contato_recado')
        }),
        ('Mais informações', {
            'classes': ('grp-collapse grp-closed',),
            'fields': (
            'motivo_consulta', 'outra_consulta', 'acompanhamento', 'medicamento', 'desejo', 'aumentar_comport',
            'diminuir_comport'),
        }),
    )
    search_fields = ('nome',)
    list_filter = (
        'nome',
        'created',
    )


admin.site.register(Paciente, PacienteAdmin)


@admin.register(Prontuario)
class ProntuarioAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'dataconsulta',)
    date_hierarchy = ('dataconsulta')
    list_filter = (
        'dataconsulta',
    )


admin.site.site_header = 'DoctorWeb'  # default: "Django Administration"
admin.site.index_title = 'Módulos'  # default: "Site administration"
admin.site.site_title = 'DoctorWeb'  # default: "Django site admin"

'''
@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):

   fieldsets = (
        ('teste', {
            'fields': (('nome', 'grupo', 'cel'), 'datanasc')
        }),
        ('Advanced options', {
            'classes': ('collapse', 'wide'),
            'fields': (('email', 'escolaridade'), 'cpf2'),
        }),

    )


    class="module aligned collapse collapsed"

'''