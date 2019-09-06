from django.db import models

# Create your models here.

class User(models.Model):

    # Definimos los campos del modelo
    iduser = models.AutoField(primary_key = True)
    name_user = models.CharField(max_length = 254)
    email_user = models.CharField(max_length = 254)
    phone_user = models.CharField(max_length = 20, default = '')


    def __str__(self):
        return self.name_user

