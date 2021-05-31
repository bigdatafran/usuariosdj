from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth  import authenticate # Nueva importación para hacer funciones de autenticación
from django.contrib.auth  import login, logout # Con esta función haremos el login, y el logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from django.http import HttpResponseRedirect #Para redirigir a otra página

# Create your views here.
from django.views.generic import(
    View, # Es la vista padre de todas las demás vistas y se utiliza aquí para hacer un logout
    CreateView
)

from django.views.generic.edit import(
    FormView
)

from .forms import (
    UserRegisterForm, 
    LoginForm,
    UpdatePasswordForm,
    VerificationForm
)

from .models import User
from .functions import code_generator

class UserRegisterView(FormView):
    
    template_name = "users/register.html"
    form_class = UserRegisterForm
    success_url = '/'

    def form_valid(self,form):
        # generamos el código que enviamos al usuario para que se autentique para su alta como usuario
        codigo = code_generator()
        User.objects.cerate_user( #Para reutilizar un manager creado anteriormente
            form.cleaned_data['username'], #para recuperar este campo del formulario
            form.cleaned_data['email'], 
            form.cleaned_data['password1'], 
            nombres = form.cleaned_data['nombres'],
            apellidos =form.cleaned_data['apellidos'],
            genero =form.cleaned_data['genero'],
            codregistro = codigo # Cada vez registro un usuario automaticamente le asigna un código aleatorio.
        )
        # enviar el código el email facilitado por el usuario
        asunto = 'confirmación de email'
        mensaje = 'Código de verificación: '+ codigo
        email_remitente = 'frrgcsocial@gmail.com'
        # Los atributos para mandar el correo los configuro en settings en el local.py
        send_mail(asunto, mensaje, email_remitente,[form.cleaned_data['email'],])
        # Ahora hay que redirigir a la pantalla de validación para ingreasr el código que se ha enviado al correo

        #return super(UserRegisterView,self).form_valid(form)
        return HttpResponseRedirect( # Tendremso que construir una vista para que el usuario pueda pegar el código que se le ha enviado
            reverse(
                'users_app:user-verification'
            )

        )


class LoginUser(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home_app:panel')

    def form_valid(self,form):
        user = authenticate( # Con esto se recupera un usuario que ya esté en la base de datos.
            
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password']
            #Hasta aquí no se ha hecho el login, sólo se ha verificado
        )
        #Ahora hariamos el login, y django crea un usuario que estará activo para toda la sesión.
        #Para ello se utiliza la siguiente función
        login(self.request, user) # Con todo esto ya estaría completado el proceso del login

        return super(LoginUser,self).form_valid(form)


#Esta clase es para hacer logout
class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'users_app:user-login'
            )

        )

# Esta vista es para cmabiar el password del usuario
class UpdatePasswordView(LoginRequiredMixin,FormView):
    template_name = 'users/update.html'
    form_class = UpdatePasswordForm
    success_url = reverse_lazy('users_app:user-login')
    login_url = reverse_lazy('users_app:user-login')


    def form_valid(self,form):
        usuario = self.request.user # recupero el usuario que está activo en este momento
        user = authenticate( # Con esto se recupera un usuario que ya esté en la base de datos.
            
            username = usuario.username,
            password = form.cleaned_data['password1']
            #Hasta aquí no se ha hecho el login, sólo se ha verificado
        )
        # ai la autenticación es correcta el user tiene algo
        if user:
            new_password = form.cleaned_data['password2']
            usuario.set_password(new_password)
            usuario.save()

        logout(self.request) #quiero hacer un cerre de sesión para que se acceda con el nuevo password

        return super(UpdatePasswordView,self).form_valid(form)


# Creación de la vista para que el usuario que se está dando de alta ingrese el código enviado por mail

class CodeVerificationView(FormView):
    template_name = 'users/verification.html'
    form_class = VerificationForm
    success_url = reverse_lazy('users_app:user-login')

    def form_valid(self,form):
        

        return super(CodeVerificationView,self).form_valid(form)
