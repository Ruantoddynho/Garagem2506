from django.db import models

from .acessorio import Acessorio
from .cor import Cor
from .modelo import Modelo


class Veiculo(models.Model):
    modelo = models.ForeignKey(Modelo, on_delete=models.RESTRICT)
    cor = models.ForeignKey(Cor, on_delete=models.RESTRICT)
    acessorio = models.ForeignKey(Acessorio, on_delete=models.RESTRICT)
    ano = models.IntegerField(default=0, null=True, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)
    
    def __str__(self):
        return f"{self.modelo} {self.ano} {self.cor}"