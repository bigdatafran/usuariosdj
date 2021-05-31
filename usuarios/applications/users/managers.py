# Hay que redefinir las siguientes funciones
from django.db import models
from django.contrib.auth.models import BaseUserManager 

class UserManager(BaseUserManager, models.Manager):

    #is_staff para definir si el ususario puede o no acceder al administrador de django
    def _create_user(self, username, email, password, is_staff,is_superuser,**extra_fields):
        user = self.model(
            username= username,
            email = email,
            is_staff = is_staff, #para definir si el ususario puede o no acceder al administrador, esun booleano
            is_superuser = is_superuser,
            **extra_fields
        )
        # se necesita que el password se encripte, para ellos se utiliza la siguiente función
        user.set_password(password)
        user.save(using = self.db) #Guardamos en la base datos
        return user

    #sobreescribimos esta función para la gestión usuarios
    #def create_user(self): #A esta función se le llama cuando se crea un usuario en el proyecto

    def create_superuser(self,username,email,password=None, **extra_fields): #para crear superusuarios
        # se passa True y True porque el usuario que estamos creando puede acceder a la administración django y es superusuario
        return self._create_user(username, email, password, True, True, **extra_fields)

    # Ahora creamos un usuario normal
    def cerate_user(self,username, email,password=None,**extra_fields):
        return self._create_user(username,email,password,False,False,**extra_fields)