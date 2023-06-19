from django.urls import path
from .views import UserUpdateView, ChangerPasswordView, SuccessView, ResetCompletView, ResetConfirmView, ResetSuccessView, ResetView

app_name = 'users'

urlpatterns = [
    path('compte/modifier/<int:pk>/', UserUpdateView.as_view(), name='compte'),
    path('compte/changer-mot-de-passe/', ChangerPasswordView.as_view(), name='password_change'),
    path('compte/changer-mot-de-passe/succes/', SuccessView.as_view(), name='password_change_success'),
    #template_name='log/password_change_success.html'
    path('compte/renitialiser-mot-de-passe/', ResetView.as_view(), name='password_reset'),
    path('compte/renitialiser-mot-de-passe/succes/', ResetSuccessView.as_view(), name='password_reset_sucess'),
    path('compte/renitialiser-mot-de-passe/confirmer/', ResetConfirmView.as_view(), name='password_reset_confirmer'),
    path('compte/renitialiser-mot-de-passe/completer/', ResetCompletView.as_view(), name='password_reset_completer'),

]