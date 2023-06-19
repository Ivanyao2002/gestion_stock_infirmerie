from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView,PasswordResetDoneView,PasswordResetCompleteView,PasswordResetConfirmView
from django.http import JsonResponse

from .forms import ConnexionForm, ChangeForm, PassWordForm, ResetForm, SetForm
from .models import User

# Create your views here.

class Connexion(LoginView):
    template_name = 'log/login.html'
    form_class = ConnexionForm
  
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
    
class ResetView(PasswordResetView):
    template_name = 'reset/reset.html'
    form_class = ResetForm
    success_url = reverse_lazy('users:password_reset_sucess')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs
        
class ResetConfirmView(PasswordResetConfirmView):
    template_name = 'reset/reset_confirm.html'
    form_class = SetForm
    success_url = reverse_lazy('users:password_reset_completer')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

class ResetCompletView(PasswordResetCompleteView):
    template_name = 'reset/reset_complete.html'

class ResetSuccessView(PasswordResetDoneView):
    template_name = 'reset/reset_done.html'