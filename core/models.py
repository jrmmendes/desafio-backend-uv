from django.db import models


class Processo(models.Model):
    """
    Model que representa um processo
    """
    pasta = models.CharField(
        blank=False,
        max_length=100,
    )

    comarca = models.CharField(
        max_length=100,
    )

    uf = models.CharField(
        max_length=2,
    )
