from django.db import models

# Create your models here.

class Registration(models.Model):
    name=models.CharField(max_length=100, blank=False,null=False)
    rollNo=models.IntegerField(blank=False, null= False, unique=True)
    email = models.EmailField(max_length=100, blank= False, null=False, unique=True)
    phone = models.IntegerField(blank = False, null = False)
    branch = models.CharField(max_length=100,blank=False, null = False)
    role= models.CharField(max_length=100,blank=True, null=True)
    year = models.CharField(max_length=100,blank=True, null=True)
    link =models.CharField(max_length=100,blank=True, null=True)
    def __str__(self):
        return f'{self.name} ({self.email})'




    