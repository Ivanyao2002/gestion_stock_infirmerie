from django.urls import path
from .views import UserUpdateView, ChangerPasswordView, SuccessView

app_name = 'users'

urlpatterns = [
    path('account/update_<int:pk>/', UserUpdateView.as_view(), name='compte'),
    path('account/alter_password/', ChangerPasswordView.as_view(), name='password_change'),
    path('account/alter_password_success/', SuccessView.as_view(), name='password_change_success'),
]