from django.db import models
from django.contrib.auth.models import User

class Avaliacao(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField(null=True, blank=True)
    nota = models.DecimalField(max_digits=3, decimal_places=2)
    data = models.DateTimeField()

    def __str__(self):
        return f"Usuário: {self.user} - Comentário: {self.comentario} - Nota: {self.nota} - Data: {self.data}"
