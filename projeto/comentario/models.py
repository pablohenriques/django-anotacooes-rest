from django.db import models
from django.contrib.auth.models import User

class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()
    data = models.DateTimeField()

    def __str__(self):
        return f"Usuário: {self.usuario} - Comentário: {self.comentario} - Data: {self.data}"
