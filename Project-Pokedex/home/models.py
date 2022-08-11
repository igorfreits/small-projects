from django.db import models

# Create your models here.

class dados_pokemon(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    tipo = models.CharField(max_length=100, verbose_name='Tipo')
    descricao = models.CharField(max_length=100, verbose_name='Descrição')
    imagem = models.ImageField(upload_to='pokemon', verbose_name='Imagem')
    number = models.IntegerField(verbose_name='Número')
    def __str__(self):
        return self.nome