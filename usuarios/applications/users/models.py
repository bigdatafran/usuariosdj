from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager

class User(AbstractBaseUser,PermissionsMixin):

    GENDER_CHOICES=[
        ('M' , 'Masculino'),
        ('F' , 'Femenino'),
        ('O' , 'Otros'),
    ]

    

    username = models.CharField(max_length=10, unique = True)
    email = models.EmailField()
    nombres = models.CharField(max_length=30, blank = True)
    apellidos = models.CharField(max_length=30, blank= True)
    genero = models.CharField(max_length=1,choices = GENDER_CHOICES, blank= True)
    codregistro =  models.CharField(max_length=6, blank= True) # Se añade para poder enviar claves al usuario durante el proceso de registro

    # is_staff es para permitir o no que un usuario entre en el administrador de Django
    is_staff = models.BooleanField(default=False) #Este argumento booleano hay que añadirlo para que no lance un error
    is_active = models.BooleanField(default=False) #si el usuario no está verificado su valor es false, en caso contrario será true

    USERNAME_FIELD = 'username' # Atributo para hacer el login del administrador

    objects = UserManager()

    REQUIRED_FIELDS =['email',]

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.nombres + ' '+self.apellidos