from django.db import models

from .categoria import Categoria
from .marca import Marca


class Modelo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.RESTRICT)
    categoria = models.ForeignKey(Categoria, on_delete=models.RESTRICT)
    
    def __str__ (self):
        return f"{self.marca}"
    
    