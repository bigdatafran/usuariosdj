from django import forms
from django.contrib.auth  import authenticate # Nueva importación para hacer funciones de autenticación

from .models import User

class UserRegisterForm(forms.ModelForm):
    """Form definition for UserRegister."""
    # lo que sigue es para poder capturar la contraseña
    password1 = forms.CharField(
        label = 'contraseña',
        required = True,
        widget = forms.PasswordInput(
            attrs ={
                'placeholder' : 'Contraseña'
            }
        )
    )
    # Hago repetir contraseña para verificar que la contraseña se ha escrito correctamente.
    password2 = forms.CharField(
        label = 'contraseña',
        required = True,
        widget = forms.PasswordInput(
            attrs ={
                'placeholder' : 'Repetir Contraseña'
            }
        )
    )

    class Meta:
        """Meta definition for UserRegisterform."""

        model = User
        #fields = ('__all__')
        fields = (
            'username',
            'email',
            'nombres',
            'apellidos',
            'genero',
        )

    # Para validar el password
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            # para aññadir este error al resto de errores que see muestran por fdefecto en el formulario
            self.add_error('password2','Las contraseñas no son iguales')
        #compruebo que las contraseñas no tienen menos de 5 dígitos
        if len(self.cleaned_data['password1']) <=5:
            self.add_error('password1','La contraseña debe tener una longitud mayor que 5 caracteres')
        


class LoginForm(forms.Form):
    username = forms.CharField(
        label = 'username',
        required = True,
        widget = forms.TextInput(
            attrs ={
                'placeholder' : 'username'
            }
        )
    )    
    password = forms.CharField(
        label = 'contraseña',
        required = True,
        widget = forms.PasswordInput(
            attrs ={
                'placeholder' : 'Contraseña'
            }
        )
    )

    def clean(self) : # Para hacer una validación de los datos
        cleaned_data = super(LoginForm,self).clean
        username =  self.cleaned_data['username']       
        password =  self.cleaned_data['password']       

        if not authenticate(username = username, password = password): # si no me devuelto un usuario
            raise forms.ValidationError('Los datos del usuario no son correctos')

        return self.cleaned_data

    
class UpdatePasswordForm(forms.Form):

    password1 = forms.CharField(
        label = 'contraseña',
        required = True,
        widget = forms.PasswordInput(
            attrs ={
                'placeholder' : 'Contraseña actual'
            }
        )
        
    )
    password2 = forms.CharField(
        label = 'contraseña',
        required = True,
        widget = forms.PasswordInput(
            attrs ={
                'placeholder' : 'Contraseña nueva'
            }
        )
        
    )

#Formulario para ingresar las claves enviadas al usuario que se está dando de alta
class VerificationForm(forms.Form):
    codregistro = forms.CharField(required = True)