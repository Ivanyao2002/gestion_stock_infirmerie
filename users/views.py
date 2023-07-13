from django.shortcuts import render, redirect
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.http import JsonResponse

from .forms import ConnexionForm, ChangeForm, PassWordForm
from .models import User

# Create your views here.

class Connexion(LoginView):
    template_name = 'log/login.html'
    form_class = ConnexionForm
    success_url = reverse_lazy('stocks:list_medocs')#Redirection par defaut après authentification

    # Redirection personnalisé après authentification pour les users appartenant au groupe Users 
    def get_success_url(self):
        user = self.request.user
        if user.groups.filter(name='Users').exists():
            return reverse_lazy('consultation:list_consultation_jour')
        return self.success_url

  
class Deconnexion(LogoutView):
    pass

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'log/update_user.html'
    form_class = ChangeForm
    success_url = reverse_lazy('stocks:list_medocs')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs
    
    def get_success_url(self):
        user = self.request.user
        if user.groups.filter(name='Users').exists():
            return reverse_lazy('consultation:list_consultation_jour')
        return self.success_url
    
class ChangerPasswordView(LoginRequiredMixin, PasswordChangeView):
    model = User
    form_class = PassWordForm
    template_name = 'log/change_password.html'
    success_url = reverse_lazy('password_change_success')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

class SuccessView(LoginRequiredMixin, PasswordChangeDoneView):
    def get(self, request, *args, **kwargs):
        message = 'Votre mot de passe a été modifié avec succès.'
        return JsonResponse({'message': message})  
