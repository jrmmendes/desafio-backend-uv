from django.contrib import admin
from .models import Planilha


admin.site.register(
    Planilha,
    verbose_name='planilha',
    verbose_name_plural='planilhas',
)
