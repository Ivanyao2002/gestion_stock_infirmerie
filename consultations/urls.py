from django.urls import path
from .views import DayConsultationCreateView, DayConsultationListView, PeriodicConsultationListView, DayConsultationDetailView, PeriodicConsultationDetailView, PeriodicConsultationCreateView, get_nom_from_matricule, PeriodicConsultationUpdateView, DayConsultationUpdateView

app_name = 'consultation'

urlpatterns = [
    path('new_day_consultation/', DayConsultationCreateView.as_view(), name='consultation_jour'),
    path('new_vma_consultation/',PeriodicConsultationCreateView.as_view(),name='consultation_vma'),
    path('list_day_consultation/', DayConsultationListView.as_view(), name='list_consultation_jour'),
    path('list_vma_consultation/',PeriodicConsultationListView.as_view(),name='list_consultation_vma'),
    path('detail_vma_consultation_<int:pk>/',PeriodicConsultationDetailView.as_view(),name='detail_consultation_vma'),
    path('detail_day_consultation_<int:pk>/',DayConsultationDetailView.as_view(),name='detail_consultation_jour'),
    path('get_nom/', get_nom_from_matricule, name='get_nom'),    
    path('update_break_day_consultation/<int:pk>/',DayConsultationUpdateView.as_view(),name='update_consultation_breakday'),
    path('update_break_periodic_consultation/<int:pk>/',PeriodicConsultationUpdateView.as_view(),name='update_consultation_breakperiodic'),
]