from django.db import models
from django.contrib.auth.models import User

# Create class Categoria.
class Categoria(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)
    
    def __str__(self):
        return self.nome
    
# Create class Flashcard.
class Flashcard(models.Model):
    DIFICULDADE_CHOICES = (('D', 'Difícil'), ('M', 'Médio'), ('F', 'Fácil'))
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    pergunta = models.CharField(max_length=100)
    resposta = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    dificuldade = models.CharField(max_length=1, choices=DIFICULDADE_CHOICES)
    def __str__(self):
     return self.pergunta
