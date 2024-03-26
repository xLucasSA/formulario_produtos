from django.db import models

class Produto(models.Model):
    id= models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, null=False, blank=False)
    descricao = models.TextField(blank=False, null=False)
    valor = models.FloatField(null=False, blank=False)
    disponivel = models.BooleanField(null=False, blank=False, choices=[(True, 'Sim'), (False, 'Não')])

    def __str__(self) -> str:
        return self.nome

    class Meta:
        ordering = ['valor']

    def save(self, *args, **kwargs):
        
        if self.valor < 0:
            return
           
        super().save(*args, **kwargs)