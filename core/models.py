from django.db import models


class Processo(models.Model):
    """
    Model que representa um processo
    """
    pasta = models.TextField()
    comarca = models.TextField()
    uf = models.TextField()
