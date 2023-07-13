from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from .models import Consultation_journaliere, Consultation_VMA
from .forms import Consultation_JourForm, Consultation_VmaForm
from stocks.models import Travailleurs

# Create your views here.
class ConsultationCreateView(LoginRequiredMixin, CreateView):
    model = Consultation_journaliere
    template_name = "day_create.html"
    form_class = Consultation_JourForm
    success_url = reverse_lazy('consultation:list_consultation_jour')

class ConsultationVmaCreateView(LoginRequiredMixin, CreateView):
    model = Consultation_VMA
    template_name = "vma_create.html"
    form_class = Consultation_VmaForm
    success_url = reverse_lazy('consultation:list_consultation_vma')

    def form_valid(self, form):
        travailleur = form.cleaned_data.get('travailleurs')
        nom = form.cleaned_data.get('nom_prenoms')
        societe = form.cleaned_data.get('societe')
        atelier = form.cleaned_data.get('atelier')

        if travailleur is None and nom and societe and atelier:
            travailleur = Travailleurs.objects.create(nom=nom, societe=societe, atelier=atelier)

        form.instance.travailleurs = travailleur
        return super().form_valid(form)
    
class ConsultationDayView(LoginRequiredMixin, ListView):
    model = Consultation_journaliere
    template_name = "day_list.html"
    context_object_name = "days"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        consult = Consultation_journaliere.objects.all()
        paginator = Paginator(consult, 10) 
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['days'] = page_obj
        return context
    
    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            return self.post(request, *args, **kwargs)
        else:
            return self.get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Gérer la logique pour les requêtes POST ici
        date = request.POST.get('date')
        mois = request.POST.get('mois')
        annee = request.POST.get('annee')
        consult = request.POST.get('consult')
        matricule = request.POST.get('matricule')

        days = Consultation_journaliere.objects.all()
    
        if date:
            days = Consultation_journaliere.search_by_date(date)
        if mois:
            days = Consultation_journaliere.search_by_month(mois)
        if annee:
            days = Consultation_journaliere.search_by_year(annee)
        if consult:
            days = Consultation_journaliere.search_by_name(consult)
        if matricule:
            days = Consultation_journaliere.search_by_matricule(matricule)

        context = {
            'days': days
        }

        return render(request, 'day_list.html', context)
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

class ConsultationVmaView(LoginRequiredMixin, ListView):
    model = Consultation_VMA
    template_name = "vma_list.html"
    context_object_name = "vma"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        consult = Consultation_VMA.objects.all()
        paginator = Paginator(consult, 10) 
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['vma'] = page_obj
        return context
    
    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            return self.post(request, *args, **kwargs)
        else:
            return self.get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Gérer la logique pour les requêtes POST ici
        date = request.POST.get('date')
        mois = request.POST.get('mois')
        annee = request.POST.get('annee')
        consult = request.POST.get('consult')
        matricule = request.POST.get('matricule')

        vma = Consultation_VMA.objects.all()
    
        if date:
            vma = Consultation_VMA.search_by_date(date)
        if mois:
            vma = Consultation_VMA.search_by_month(mois)
        if annee:
            vma = Consultation_VMA.search_by_year(annee)
        if consult:
            vma = Consultation_VMA.search_by_name(consult)
        if matricule:
            vma = Consultation_VMA.search_by_matricule(matricule)

        context = {
            'vma': vma
        }

        return render(request, 'vma_list.html', context)
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

class ConsultationVmaDetailView(LoginRequiredMixin, DetailView):
    model = Consultation_VMA
    template_name = "vma_detail.html"
    context_object_name = "details"

class ConsultationJourDetailView(LoginRequiredMixin, DetailView):
    model = Consultation_journaliere
    template_name = "jour_detail.html"
    context_object_name = "details"
    