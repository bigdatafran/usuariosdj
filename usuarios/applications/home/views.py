
import datetime
from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from django.views.generic import(
    TemplateView
)

# Create your views here.
 
class HomePage(LoginRequiredMixin, TemplateView): # Con esto protejo esta vista para solo verla usuario logeado
     template_name = "home/index.html"
     login_url = reverse_lazy('users_app:user-login')


class FechaMixin(object): #Con esto vamos a crer un mixing

    def get_context_data(self, **kwargs):
        context = super(FechaMixin, self).get_context_data(**kwargs)
        context['fecha'] = datetime.datetime.now()
        return context
    

#Ahora creo un mixing con el TemplateView
class TemplatePruebaMixin(FechaMixin, TemplateView): #El/los mixing padre siempre delante
    template_name = "home/mixin.html"
    