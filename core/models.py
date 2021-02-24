from django.db import models

# Create your models here.


class Produto(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=9)
    estoque = models.IntegerField('Quantidade em estoque')

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('Email', max_length=100)


    def __str__(self):
        return f'{self.nome} {self.sobrenome}'