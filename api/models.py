from django.db import models

# Create your models here.

class Registration(models.Model):
    name=models.CharField(max_length=100, blank=False,null=False)
    rollNo=models.IntegerField(max_length=6, blank=False, null= False)
    email = models.EmailField(max_length=100, blank= False, null=False)
    phone = models.IntegerField(max_length=10, blank = False, null = False)
    branch = models.CharField(max_length=200,blank=False, null = False)

    def __str__(self):
        return f'{self.name} Email: {self.email}'


    