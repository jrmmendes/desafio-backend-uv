from django.db import models


class Planilha(models.Model):
    """
    Model que representa uma planilha
    """
    nome = models.CharField(
        blank=False,
        max_length=256,
    )

    cliente = models.CharField(
        blank=False,
        max_length=256,
    )

    arquivo = models.FileField(blank=False)

    def __str__(self):
        return self.nome + '(' + self.cliente + ')'
