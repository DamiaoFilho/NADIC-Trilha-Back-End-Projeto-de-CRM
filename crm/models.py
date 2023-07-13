from django.db import models

from django.contrib.auth.models import AbstractUser


# Create your models here.

class Company(models.Model):
    """Model para criação de empresas com seu nome e faturamento"""
    name = models.CharField(max_length=100, verbose_name="Nome")
    balance = models.DecimalField(max_digits=100,decimal_places=2, verbose_name="Nome")

    def __str__(self) -> str:
        return self.name

class Stock(models.Model):
    """Model para a criação de estoque de um produto com seu nome, preço, quantidade e categoria"""
    name = models.CharField(max_length=100, verbose_name="Nome")
    price = models.DecimalField(max_digits=100,decimal_places=2, verbose_name="Preço")
    image = models.ImageField(upload_to="StockImages", verbose_name="Imagem do produto", default=None)
    quantity = models.IntegerField()
    category = models.ForeignKey("Category", on_delete=models.CASCADE, verbose_name="Categoria")
    company = models.ForeignKey("Company", on_delete=models.CASCADE, verbose_name="Companhia")

    def __str__(self) -> str:
        return self.name

class Category(models.Model):
    """Model para a criação de diferentes categorias de produtos"""
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name 