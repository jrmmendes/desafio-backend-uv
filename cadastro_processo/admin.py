import csv
from django.contrib import admin
from django.core.files.storage import default_storage

from .models import Planilha
from core.models import Processo


def register_processes_from_csv(modeladmin, request, queryset):
    """
    Ação para registrar processos vindos de uma planilha. Ignora a primeira
    linha, pois é entendido que será o cabeçalho.
    """
    for planilha in queryset:
        processes_csv_url = planilha.arquivo.name
        with default_storage.open(processes_csv_url, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=';')
            next(reader, None)
            for row in reader:
                pasta, comarca, uf = row

                Processo.objects.create(
                    pasta=pasta,
                    comarca=comarca,
                    uf=uf
                )


register_processes_from_csv.short_description = 'Registrar processos das planilhas\
    selecionadas'


class PlanilhaAdmin(admin.ModelAdmin):
    actions = [register_processes_from_csv]


admin.site.register(
    Planilha,
    PlanilhaAdmin,
    verbose_name='planilha',
    verbose_name_plural='planilhas',
)
