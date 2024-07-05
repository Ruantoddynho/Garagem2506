from django.db import models
from .marca import Marca
from .categoria import Categoria

class Modelo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.RESTRICT)
    categoria = models.ForeignKey(Categoria, on_delete=models.RESTRICT)
    
    def __str__ (self):
        return f"{self.marca} ({self.id})"
    
    