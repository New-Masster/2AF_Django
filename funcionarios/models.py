from django.db import models

class Funcionario(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14)
    tempo_de_servico = models.IntegerField()
    ativo = models.BooleanField()
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    foto = models.ImageField(upload_to='funcionarios', null=True, blank=True)


    def __str__(self):
        return self.nome + ' ' + self.sobrenome

class Dependente(models.Model):
    nome = models.CharField(max_length=255)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nome

class Departamento(models.Model):
    nome = models.CharField(max_length=255)
    funcionarios = models.ManyToManyField(Funcionario)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    def _str_(self):
        return self.nome
