from django.db import models
from multiselectfield import MultiSelectField

from stocks.models import Travailleurs
from users.models import User

# Create your models here.
class Periodic_Consultation(models.Model):
    pathologies = (
        ('Cardiologie','Cardiologie'),
        ('Dermatologie','Dermatologie'),
        ('Digestive','Digestive'),
        ('Endocrinienne','Endocrinienne'),
        ('Endocrinologie','Endocrinologie'),
        ('Gastro-enterologie','Gastro-entérologie'),
        ('Gynecologie','Gynécologie'),
        ('Hematologie','Hématologie'),
        ('Maladies Infectieuses','Maladies Infectieuses'),
        ('Nephrologie','Néphrologie'),
        ('Neurologie','Neurologie'),
        ('ORL','ORL'),
        ('Ophtalmologie','Ophtalmologie'),
        ('Pneumologie','Pneumologie'),
        ('Psychiatrie','Psychiatrie'),
        ('Rhumatologie','Rhumatologie'),
        ('Stomatologie','Stomatologie'),
        ('Traumatologie','Traumatologie'),
        ('Urologie','Urologie'),
        ('Autres','Autres'),
    )

    examens = (
        ('Audiometrie','Audiometrie'),
        ('ECG','ECG'),
        ('Examen ophtalmologique','Examen ophtalmologique'),
        ('NFS, glycenie, proteinurie, glucosurie','NFS, glycénie, protéinurie, glucosurie'),
        ('Numeration formule sanguine','Numération formule sanguine'),
        ('Radiographie des sinus-blondeau','Radiographie des sinus-blondeau'),
        ('Radiographie pulmonaire','Radiographie pulmonaire'),
        ('Spirometrie','Spirométrie'),
        ('Transaminases, uree et creatine','Transaminases, urée et créatine'),
        ('Autres','Autres'),
    )

    motifs = (
        ('Surveillance medicale annuelle','Surveillance médicale annuelle'),
        ('Surveillance medicale particuliere/specifique','Surveillance médicale particulière/spécifique'),
        ('Surveillance medicale occasionnelle','Surveillance médicale occasionnelle'),
    )

    risques = (
        ('Nuisance Sonore','Nuisance Sonore'),
        ('Risques lies aux Fumees et Vapeurs Toxiques','Risques liés aux fumées et vapeurs toxiques'),
        ('Risques lies aux poussieres de bois','Risques liés aux poussières de bois'),
        ('Risques lies aux poussieres de sable','Risques liés aux poussières de sable'),
        ('Risques lies aux peintures (diluants, solvants) et vernis','Risques liés aux peintures (diluants, solvants) et vernis'),
        ('Risques lies aux emanations de debris de metaux','Risques liés aux émanations de débris de métaux'),
        ('Risques lies a la plongee (profondeur moins de 15 metres)','Risques liés a la plongée (profondeur moins de 15 mètres)'),
        ('Risques lies aux huiles usagees et degraissants (solvants)','Risques liés aux huiles usagées et dégraissants (solvants)'),
    )

    aptitudes = (
        ('APTE','APTE'),
        ('APTE : avec amenagement','APTE : avec aménagement'),
        ('APTE : avec recommendation','APTE : avec récommendation'),
        ('INAPTE : definitif','INAPTE : définitif'),
        ('INAPTE : temporaire','INAPTE : temporaire'),
        ('INAPTE: au poste mais apte a un autre poste','INAPTE: au poste mais apte a un autre poste'),
    )

    matricule = models.CharField(max_length=50)
    nom_prenoms = models.CharField(max_length=200)
    societe = models.CharField(max_length=50, choices=Travailleurs.choix, blank=True)
    atelier = models.CharField(max_length=100, choices=Travailleurs.departement, blank=True)
    consultation_date = models.DateField(auto_now_add=True)
    pathology = MultiSelectField(choices= pathologies, max_length=100, blank=True)
    other_pathology = models.CharField(max_length=100, blank=True)
    exam = MultiSelectField(choices=examens, max_length=100, blank=True)
    other_exam = models.CharField(max_length=100, blank=True)
    risks = MultiSelectField(choices=risques, max_length=100, blank=True)
    reasons = models.CharField(max_length=100, choices=motifs)
    aptitude = models.CharField(max_length=100, choices=aptitudes)
    break_day = models.PositiveBigIntegerField(blank=True, null=True)
    evacuation = models.BooleanField(default=False)
    observations = models.TextField(blank=True)
    prescription = models.TextField(max_length=200, blank=True, default="")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


    class Meta:
        ordering = ['consultation_date']
        verbose_name_plural = 'Consultations Périodiques'

    def __str__(self):
        return f"Consultation périodique du {self.consultation_date} pour {self.nom_prenoms}"
    
    @classmethod
    def search_by_date(cls, date):
        return cls.objects.filter(consultation_date=date)
    
    @classmethod
    def search_by_month(cls, mois):
        return cls.objects.filter(consultation_date__month=mois)

    @classmethod
    def search_by_year(cls, année):
        return cls.objects.filter(consultation_date__year=année)

    @classmethod
    def search_by_name(cls, nom):
        return cls.objects.filter(nom_prenoms__icontains=nom)
    
    @classmethod
    def search_by_matricule(cls, matricule):
        return cls.objects.filter(matricule=matricule) 
   
    # def save(self, *args, **kwargs):
    #     request = kwargs.pop('request', None)
    #     self.user = request.user if request else None 
    #     if not self.break_day:
    #         self.break_day = 0
    #     return super().save(*args, **kwargs)
    
    # def save(self, *args, **kwargs):
    #     request = kwargs.pop('request', None)  # Récupère l'objet request s'il existe
    #     self.user = request.user if request else None  # Assigne l'utilisateur connecté ou None
    #     super().save(*args, **kwargs)

class Day_Consultation(models.Model):
    pathologies = (
        ('Cardiologie','Cardiologie'),
        ('Dermatologie','Dermatologie'),
        ('Digestive','Digestive'),
        ('Endocrinienne','Endocrinienne'),
        ('Endocrinologie','Endocrinologie'),
        ('Gastro-enterologie','Gastro-entérologie'),
        ('Gynecologie','Gynécologie'),
        ('Hematologie','Hématologie'),
        ('Maladies Infectieuses','Maladies Infectieuses'),
        ('Nephrologie','Néphrologie'),
        ('Neurologie','Neurologie'),
        ('ORL','ORL'),
        ('Ophtalmologie','Ophtalmologie'),
        ('Pneumologie','Pneumologie'),
        ('Psychiatrie','Psychiatrie'),
        ('Rhumatologie','Rhumatologie'),
        ('Stomatologie','Stomatologie'),
        ('Traumatologie','Traumatologie'),
        ('Urologie','Urologie'),
        ('Autres','Autres'),
    )

    lesions = (
        ('Amputation','Amputation'),
        ('Atteinte oculaire','Atteinte oculaire'),
        ('Contusion','Contusion'),
        ('Entorse','Entorse'),
        ('Fracture','Fracture'),
        ('Plaie','Plaie'),
        ('Plaie Traumatique','Plaie Traumatique'),
        ('Autres','Autres'),
    )

    motifs = (
        ('Accidents','Accidents'),
        ('Consultation generale','Consultation générale'),
        ("Visite d'embauche","Visites d'embauche"),
        ('Visite de reprise de travail apres maladie','Visite de reprise de travail après maladie'),
        ('Visite de reprise de travail apres maternite','Visite de reprise de travail après maternité'),
        ('Visite de reprise de travail apres conge annuel','Visite de reprise de travail après congé annuel'),
        ('Visite de reprise de travail apres accident du travail','Visite de reprise de travail après accident du travail'),
        ('Visite de reprise de travail apres maladie professionnelle','Visite de reprise de travail après maladie professionnelle'),
        ('Visite occasionnelle','Visite occasionnelle'),
    )

    accidents = (
        ('Accident reel','Accident réel'),
        ('Accident du trajet','Accident du trajet'),
        ('Accident a la declaration dans le delai de carence de la CNPS','Accident à la déclaration dans le délai de carence de la CNPS'),
    )

    arrets = (
        ('Avec arret','Avec arrêt'),
        ('Sans arret','Sans arrêt'),
    )

    sieges = (
        ('Membre superieur','Membre supérieur'),
        ('Membre inferieur','Membre inférieur'),
        ('Tete','Tête'),
        ('Thorax','Thorax'),
        ('Autres','Autres'),
    )
    
    aptitudes = (
        ('APTE','APTE'),
        ('APTE : avec amenagement','APTE : avec aménagement'),
        ('APTE : avec recommendation','APTE : avec récommendation'),
        ('INAPTE : definitif','INAPTE : définitif'),
        ('INAPTE : temporaire','INAPTE : temporaire'),
        ('INAPTE: au poste mais apte a un autre poste','INAPTE: au poste mais apte a un autre poste'),
    )

    matricule = models.CharField(max_length=50)
    nom_prenoms = models.CharField(max_length=200)
    societe = models.CharField(max_length=50, choices=Travailleurs.choix, blank=True)
    atelier = models.CharField(max_length=100, choices=Travailleurs.departement, blank=True)
    consultation_date = models.DateField(auto_now_add=True)
    pathology = MultiSelectField(choices=pathologies, max_length=100, blank=True)
    other_pathology = models.CharField(max_length=100, blank=True)
    accident = models.CharField(max_length=100, choices=accidents, blank=True)
    stop = models.CharField(max_length=50, choices=arrets, blank=True)
    lesion = models.CharField(max_length=100, choices=lesions, blank=True)
    other_lesion = models.CharField(max_length=100, blank=True)
    siege = models.CharField(max_length=100, choices=sieges, blank=True)
    other_siege = models.CharField(max_length=100, blank=True)
    reasons = models.CharField(max_length=100, choices=motifs)
    aptitude = models.CharField(max_length=100, choices=aptitudes)
    break_day = models.PositiveBigIntegerField(blank=True, null=True)
    evacuation = models.BooleanField(default=False)
    observations = models.TextField(blank=True)
    prescription = models.TextField(max_length=200, blank=True, default="")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['consultation_date']
        verbose_name_plural = 'Consultations Journalières'

    def __str__(self):
        return f"Consultation journalière du {self.consultation_date} pour {self.nom_prenoms}"
        
    @classmethod
    def search_by_date(cls, date):
        return cls.objects.filter(consultation_date=date)
    
    @classmethod
    def search_by_month(cls, mois):
        return cls.objects.filter(consultation_date__month=mois)

    @classmethod
    def search_by_year(cls, année):
        return cls.objects.filter(consultation_date__year=année)

    @classmethod
    def search_by_name(cls, nom):
        return cls.objects.filter(nom_prenoms__icontains=nom)
    
    @classmethod
    def search_by_matricule(cls, matricule):
        return cls.objects.filter(matricule=matricule) 
    
    def save(self, *args, **kwargs):
        request = kwargs.pop('request', None)
        self.user = request.user if request else None 
        if not self.break_day:
            self.break_day = 0
        return super().save(*args, **kwargs)
