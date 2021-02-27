from django.db import models

class Endereco(models.Model):
    endereco = models.CharField(max_length=128)
    cidade = models.CharField(max_length=128)
    estado = models.CharField(max_length=128)

    def __str__(self):
        return f"Endereco: {self.endereco} - Cidade: {self.cidade} - Estado: {self.estado}"

