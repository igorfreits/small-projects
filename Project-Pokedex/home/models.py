from django.db import models

# Create your models here.


class Pokemon(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    type = models.CharField(max_length=100, verbose_name='Tipo')
    description = models.CharField(max_length=100, verbose_name='Descrição')
    image = models.ImageField(upload_to='pokemon', verbose_name='Imagem')
    number = models.IntegerField(verbose_name='Número')
    evolution = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Evolução')
    abilities = models.CharField(max_length=100, verbose_name='Habilidades')

    def __str__(self):
        return self.nome
