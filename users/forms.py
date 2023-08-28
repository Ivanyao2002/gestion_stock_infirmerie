from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm

from .models import User

class ConnexionForm(AuthenticationForm):
    def __init__(self, request, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'type':"text",
            'class':"form-control ",
            'style':"color: black;",
            'id':"username",
            'placeholder':"Login",
        })
        self.fields['password'].widget.attrs.update({
            'type':"Password",
            'class':"form-control ",
            'style':"color: black;",
            'id':"password",
            'placeholder':"Password",
        })

class ChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request', None)#Permet d'eviter les erreurs de réquettes, on récupère la valeur de request, de kwargs sans générer d'erreur si elle n'est pas présente.Ensuite on appelle super sans request car la class UserChangeForm n'attend pas un request.
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'type':"text",
            'class':"form-control ",
            'style':"color: black;",
            'id':"username",
            'placeholder':"Login",
        })
        self.fields['email'].widget.attrs.update({
            'type':"email",
            'class':"form-control ",
            'style':"color: black;",
            'id':"email",
            'placeholder':"Email",
            'name':"email",
            'oninput':"validateEmail()", 
        })
    class Meta:
        model = User
        fields = ['username', 'email']

class PassWordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request', None)#Permet d'eviter les erreurs de réquettes, on récupère la valeur de request, de kwargs sans générer d'erreur si elle n'est pas présente.Ensuite on appelle super sans request car la class UserChangeForm n'attend pas un request.
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({
            'type':"Password",
            'class':"form-control ",
            'style':"color: black;",
            'id':"old_password",
            'placeholder':"password",
        })
        self.fields['new_password1'].widget.attrs.update({
            'type':"Password",
            'class':"form-control ",
            'style':"color: black;",
            'id':"new_password1",
            'placeholder':"Password",
        })
        self.fields['new_password2'].widget.attrs.update({
            'type':"Password",
            'class':"form-control ",
            'style':"color: black;",
            'id':"new_password2",
            'placeholder':"Password",
        })

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
