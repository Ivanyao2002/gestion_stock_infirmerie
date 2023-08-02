from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from .models import Periodic_Consultation, Day_Consultation
from .forms import DayConsultationForm, PeriodicConsultationForm, CongeForm
from stocks.models import Travailleurs


# Create your views here.
@login_required
def get_nom_from_matricule(request):
    if request.method == 'GET':
        matricule = request.GET.get('matricule')
        print(request.GET)
        try:
            travailleur = Travailleurs.objects.get(matricule=matricule)
            nom_prenoms = travailleur.nom
            societe = travailleur.societe
            atelier = travailleur.atelier
            print(nom_prenoms)
            print(societe) 
            print(atelier)
        except Travailleurs.DoesNotExist:
            nom_prenoms = "Le matricule n'existe pas. Veuillez enregistrer ce travailleur"
            societe = ""
            atelier = ""

        return JsonResponse({'nom': nom_prenoms, 'societe': societe, 'atelier': atelier,})

class DayConsultationCreateView(LoginRequiredMixin, CreateView):
    model = Day_Consultation
    template_name = "day_create.html"
    form_class = DayConsultationForm
    success_url = reverse_lazy('consultation:list_consultation_jour')

    def form_invalid(self, form):
        # Renvoie les erreurs de validation sous forme de réponse JSON
        return JsonResponse({'errors': form.errors})
    
    def form_valid(self, form):
        # Enregistrer le formulaire si valide
        self.object = form.save()
        # Renvoyer une réponse JSON avec succès
        return JsonResponse({'success': True}) 

class PeriodicConsultationCreateView(LoginRequiredMixin, CreateView):
    model = Periodic_Consultation
    template_name = "vma_create.html"
    form_class = PeriodicConsultationForm
    success_url = reverse_lazy('consultation:list_consultation_vma')
    
    def form_invalid(self, form):
        # Renvoie les erreurs de validation sous forme de réponse JSON
        return JsonResponse({'errors': form.errors})
    
    def form_valid(self, form):
        # Enregistrer le formulaire si valide
        self.object = form.save()
        # Renvoyer une réponse JSON avec succès
        return JsonResponse({'success': True})
    
class DayConsultationListView(LoginRequiredMixin, ListView):
    model = Day_Consultation
    template_name = "day_list.html"
    context_object_name = "days"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        consult = Day_Consultation.objects.all()
        paginator = Paginator(consult, 10) 
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['days'] = page_obj
        return context
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        
        if request.method == 'POST':
            return self.post(request, *args, **kwargs)
        else:
            return self.get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Gérer la logique pour les requêtes POST ici
        date = request.POST.get('date')
        mois = request.POST.get('mois')
        annee = request.POST.get('annee')
        nom = request.POST.get('nom')
        matricule = request.POST.get('matricule')

        days = Day_Consultation.objects.all()
    
        if date:
            days = Day_Consultation.search_by_date(date)
        if mois:
            days = Day_Consultation.search_by_month(mois)
        if annee:
            days = Day_Consultation.search_by_year(annee)
        if nom:
            days = Day_Consultation.search_by_name(nom)
        if matricule:
            days = Day_Consultation.search_by_matricule(matricule)

        context = {
            'days': days
        }

        return render(request, 'day_list.html', context)

class PeriodicConsultationListView(LoginRequiredMixin, ListView):
    model = Periodic_Consultation
    template_name = "vma_list.html"
    context_object_name = "vma"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        consult = Periodic_Consultation.objects.all()
        paginator = Paginator(consult, 10) 
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['vma'] = page_obj
        return context
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        
        if request.method == 'POST':
            return self.post(request, *args, **kwargs)
        else:
            return self.get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Gérer la logique pour les requêtes POST ici
        date = request.POST.get('date')
        mois = request.POST.get('mois')
        annee = request.POST.get('annee')
        nom = request.POST.get('nom')
        matricule = request.POST.get('matricule')

        vma = Periodic_Consultation.objects.all()
    
        if date:
            vma = Periodic_Consultation.search_by_date(date)
        if mois:
            vma = Periodic_Consultation.search_by_month(mois)
        if annee:
            vma = Periodic_Consultation.search_by_year(annee)
        if nom:
            vma = Periodic_Consultation.search_by_name(nom)
        if matricule:
            vma = Periodic_Consultation.search_by_matricule(matricule)

        context = {
            'vma': vma
        }

        return render(request, 'vma_list.html', context)

class PeriodicConsultationDetailView(LoginRequiredMixin, DetailView):
    model = Periodic_Consultation
    template_name = "vma_detail.html"
    context_object_name = "details"

class DayConsultationDetailView(LoginRequiredMixin, DetailView):
    model = Day_Consultation
    template_name = "jour_detail.html"
    context_object_name = "details"

class PeriodicConsultationUpdateView(LoginRequiredMixin, UpdateView):
    model = Periodic_Consultation    
    form_class = CongeForm
    template_name = "conge_periodic_update.html"
    success_url = reverse_lazy('consultation:list_consultation_vma')

    def form_invalid(self, form):
        # Renvoie les erreurs de validation sous forme de réponse JSON
        return JsonResponse({'errors': form.errors})
    
    def form_valid(self, form):
        # Enregistrer le formulaire si valide
        self.object = form.save()
        # Renvoyer une réponse JSON avec succès
        return JsonResponse({'success': True}) 


class DayConsultationUpdateView(LoginRequiredMixin, UpdateView):
    model = Day_Consultation    
    form_class = CongeForm
    template_name = "conge_day_update.html"
    success_url = reverse_lazy('consultation:list_consultation_jour')

    def form_invalid(self, form):
        # Renvoie les erreurs de validation sous forme de réponse JSON
        return JsonResponse({'errors': form.errors})
    
    def form_valid(self, form):
        # Enregistrer le formulaire si valide
        self.object = form.save()
        # Renvoyer une réponse JSON avec succès
        return JsonResponse({'success': True}) 
