from django.contrib import admin
from .models import Processo


admin.site.register(
    Processo,
    verbose_name='Processo',
    verbose_name_plural='Processos'
)
