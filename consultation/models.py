from django.db import models

from stocks.models import Travailleurs

# Create your models here.
class Consultation_journaliere(models.Model):
    affection = (
        ('CARDIO','CARDIO'),
        ('DERMATO','DERMATO'),
        ('DIGESTIVE','DIGESTIVE'),
        ('ENDOCRINIENNE','ENDOCRINIENNE'),
        ('HEMATO','HEMATO'),
        ('NEPHRO','NEPHRO'),
        ('NEURO','NEURO'),
        ('OPHTALMO','OPHTALMO'),
        ('ORL','ORL'),
        ('PNEUMO','PNEUMO'),
        ('RHUMATO','RHUMATO'),
        ('TRAUMATO','TRAUMATO'),
        ('UROLOGIQUE','UROLOGIQUE'),
        ('AUTRES','AUTRES'),
    )

    visite = (
        ('ACCIDENT','ACCIDENT'),
        ('CONSULTATION JOURNALIERE','CONSULTATION JOURNALIERE'),
        ('VISITE MEDICALE DE REPRISE : APRES ACCIDENT','VISITE MEDICALE DE REPRISE : APRES ACCIDENT'),
        ('VISITE MEDICALE DE REPRISE : APRES CONGES','VISITE MEDICALE DE REPRISE : APRES CONGES'),
        ('VISITE MEDICALE DE REPRISE : APRES MALADIE LONGUE DUREE','VISITE MEDICALE DE REPRISE : APRES MALADIE LONGUE DUREE'),
        ('VISITE MEDICALE DE REPRISE : APRES MALADIE PROFESSIONNELLE','VISITE MEDICALE DE REPRISE : APRES MALADIE PROFESSIONNELLE'),
        ('VMR APRES CONGE ANNUEL','VMR APRES CONGE ANNUEL'),
        ('VM EMBAUCHE','VM EMBAUCHE'),
        ('VM OCCASIONNELLE','VM OCCASIONNELLE'),
    )

    aptitudes = (
        ('APTE','APTE'),
        ('APTE : AVEC AMENAGEMENT','APTE : AVEC AMENAGEMENT'),
        ('INAPTE : DEFINITIF','INAPTE : DEFINITIF'),
        ('INAPTE : TEMPORAIRE','INAPTE : TEMPORAIRE'),
        ('INAPTE: AU POSTE MAIS APTE A UN AUTRE POSTE','INAPTE: AU POSTE MAIS APTE A UN AUTRE POSTE'),
    )

    date_consultation = models.DateField(auto_now_add=True)
    societe = models.CharField(max_length=50, choices=Travailleurs.choix, blank=True)
    matricule = models.CharField(unique=True, max_length=50, blank=True)
    nom_prenoms = models.CharField(max_length=200, blank=True)
    emploi_occupe = models.CharField(max_length=100, blank=True)
    atelier = models.CharField(max_length=100, choices=Travailleurs.departement, blank=True)
    type_visite = models.CharField(max_length=100, choices=visite)
    age = models.PositiveIntegerField()
    affection_connue = models.CharField(max_length=15, choices=affection)
    nouvelle_affection = models.CharField(max_length=100)
    observation = models.TextField(blank=True)
    aptitude = models.CharField(max_length=100, choices=aptitudes)
    travailleurs = models.ForeignKey(Travailleurs,on_delete= models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ["nom_prenoms"]

    def __str__(self):
        return f"Consultation journalière du {self.date_consultation} pour {self.nom_prenoms}"
    
    @classmethod
    def search_by_date(cls, date):
        return cls.objects.filter(date_consultation=date)
    
    @classmethod
    def search_by_month(cls, mois):
        return cls.objects.filter(date_consultation__month=mois)

    @classmethod
    def search_by_year(cls, année):
        return cls.objects.filter(date_consultation__year=année)

    @classmethod
    def search_by_name(cls, consult):
        return cls.objects.filter(nom_prenoms__icontains=consult)
    
    @classmethod
    def search_by_matricule(cls, matricule):
        return cls.objects.filter(matricule=matricule) 


class Consultation_VMA(models.Model):

    affection = (
        ('CARDIO','CARDIO'),
        ('DERMATO','DERMATO'),
        ('DIGESTIVE','DIGESTIVE'),
        ('ENDOCRINIENNE','ENDOCRINIENNE'),
        ('HEMATO','HEMATO'),
        ('NEPHRO','NEPHRO'),
        ('NEURO','NEURO'),
        ('OPHTALMO','OPHTALMO'),
        ('ORL','ORL'),
        ('PNEUMO','PNEUMO'),
        ('RHUMATO','RHUMATO'),
        ('TRAUMATO','TRAUMATO'),
        ('UROLOGIQUE','UROLOGIQUE'),
        ('AUTRES','AUTRES'),
    )

    visite = (
        ('VM ANNUELLE','VM ANNUELLE'),
        ('VM SPECIFIQUE','VM SPECIFIQUE'),
    )

    risques = (
        ('NUISANCE SONORE','NUISANCE SONORE'),
        ('RISQUES LIES AUX FUMEES ET VAPEURS TOXIQUES','RISQUES LIES AUX FUMEES ET VAPEURS TOXIQUES'),
        ('RISQUES LIES AUX POUSSIERES DE BOIS','RISQUES LIES AUX POUSSIERES DE BOIS'),
        ('RISQUES LIES AUX POUSSIERES DE SABLE','RISQUES LIES AUX POUSSIERES DE SABLE'),
        ('RISQUE LIE AUX PEINTURES (DILUANT, SOLVANTS) ET VERNIS','RISQUE LIE AUX PEINTURES (DILUANT, SOLVANTS) ET VERNIS'),
        ('RISQUES LIES AUX EMANATIONS DE DEBRIS DE METAUX','RISQUES LIES AUX EMANATIONS DE DEBRIS DE METAUX'),
        ('RISQUES LIES A LA PLONGEE (PROFONDEUR MOINS DE 15 METRES)','RISQUES LIES A LA PLONGEE (PROFONDEUR MOINS DE 15 METRES)'),
        ('RISQUES LIES AUX HUILES USAGEES ET DEGRAISSANTS (SOLVANTS)','RISQUES LIES AUX HUILES USAGEES ET DEGRAISSANTS (SOLVANTS)'),
    )

    aptitudes = (
        ('APTE','APTE'),
        ('APTE : AVEC AMENAGEMENT','APTE : AVEC AMENAGEMENT'),
        ('INAPTE : DEFINITIF','INAPTE : DEFINITIF'),
        ('INAPTE : TEMPORAIRE','INAPTE : TEMPORAIRE'),
        ('INAPTE: AU POSTE MAIS APTE A UN AUTRE POSTE','INAPTE: AU POSTE MAIS APTE A UN AUTRE POSTE'),
    )

    examens = (
        ('AUDIOMETRIE','AUDIOMETRIE'),
        ('BIOLOGIE(NFS, TRANSA, CREAT, AUTRES)','BIOLOGIE(NFS, TRANSA, CREAT, AUTRES)'),
        ('EXAMEN CLINIQUE','EXAMEN CLINIQUE'),
        ('OPHTALMOLOGIE(AV, FO, VC, VR)','OPHTALMOLOGIE(AV, FO, VC, VR)'),
        ('RADIOLOGIE(PULMONAIRE, BLONDEAU)','RADIOLOGIE(PULMONAIRE, BLONDEAU)'),
        ('SPIROMETRIE','SPIROMETRIE'),
    )

    date_consultation = models.DateField(auto_now_add=True)
    societe = models.CharField(max_length=50, choices=Travailleurs.choix, blank=True)
    matricule = models.CharField(blank=True, max_length=50, unique=True)
    nom_prenoms = models.CharField(max_length=200, blank=True)
    emploi_occupe = models.CharField(max_length=100, blank=True)
    atelier = models.CharField(max_length=100, choices=Travailleurs.departement, blank=True)
    type_visite = models.CharField(max_length=100, choices=visite)
    nature_risque = models.CharField(max_length=100, choices=risques, blank=True)
    age = models.PositiveIntegerField()
    examen_realise = models.CharField(max_length=100, choices=examens, blank=True)
    affection_connue = models.CharField(max_length=15, choices=affection)
    nouvelle_affection = models.CharField(max_length=100)
    observation = models.TextField(blank=True)
    aptitude = models.CharField(max_length=100, choices=aptitudes)
    travailleurs = models.ForeignKey(Travailleurs,on_delete= models.SET_NULL, null=True, blank=True)
    
    class Meta:
        ordering = ["nom_prenoms"]

    def __str__(self):
        return f"Consultation VMA du {self.date_consultation} pour {self.nom_prenoms}"
   
    @classmethod
    def search_by_date(cls, date):
        return cls.objects.filter(date_consultation=date)
    
    @classmethod
    def search_by_month(cls, mois):
        return cls.objects.filter(date_consultation__month=mois)

    @classmethod
    def search_by_year(cls, année):
        return cls.objects.filter(date_consultation__year=année)

    @classmethod
    def search_by_name(cls, consult):
        return cls.objects.filter(nom_prenoms__icontains=consult)
    
    @classmethod
    def search_by_matricule(cls, matricule):
        return cls.objects.filter(matricule=matricule) 

