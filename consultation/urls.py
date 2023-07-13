from django.urls import path
from .views import ConsultationCreateView, ConsultationDayView, ConsultationVmaCreateView, ConsultationVmaView, ConsultationJourDetailView, ConsultationVmaDetailView


app_name = 'consultation'

urlpatterns = [
    path('new_day_consultation/', ConsultationCreateView.as_view(), name='consultation_jour'),
    path('new_vma_consultation/',ConsultationVmaCreateView.as_view(),name='consultation_vma'),
    path('list_day_consultation/', ConsultationDayView.as_view(), name='list_consultation_jour'),
    path('list_vma_consultation/',ConsultationVmaView.as_view(),name='list_consultation_vma'),
    path('detail_vma_consultation_<int:pk>/',ConsultationVmaDetailView.as_view(),name='detail_consultation_vma'),
    path('detail_day_consultation_<int:pk>/',ConsultationJourDetailView.as_view(),name='detail_consultation_jour'),
]