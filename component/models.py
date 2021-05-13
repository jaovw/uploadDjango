from django.db import models
from django.contrib.auth import get_user_model



############# CAFETERIA ###############

class Produto(models.Model):

    Nome = models.CharField(max_length=100)
    Código = models.IntegerField()
    Descrição = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    apdated_at = models.DateTimeField(auto_now=True)
    
    
    


    def __str__(self):

        return self.Nome  + ' | ' + str(self.Código)
       
############ CONFEITARIA  ################         
class Produto1(models.Model):

    Nome = models.CharField(max_length=100)
    Código = models.IntegerField()
    Descrição = models.TextField()
    Ramo = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    apdated_at = models.DateTimeField(auto_now=True)


    def __str__(self):

        return self.Nome  + ' | ' + str(self.Código)
        
class Pedido(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete= models.CASCADE)
    Nome = models.ForeignKey(Produto, on_delete=models.DO_NOTHING )
    Quantidade = models.IntegerField(default=0, null=True)
    Descrição = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    apdated_at = models.DateTimeField(auto_now=True)
    nomeProduto = models.ForeignKey('Pedido',on_delete=models.CASCADE,related_name='teste')
    
    
    
    def __str__(self):
        return str(self.Nome) + ' | ' + str(self.Quantidade) +' Unidades'
    
