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

    societes = (
        ('AGENT DE BORD','AGENT DE BORD'),
        ('CARENA','CARENA'),
        ('PRESTATAIRE','PRESTATAIRE'),
        ('REGIE','REGIE'),
    )

    departement = (
        ('ADMINISTRATION','ADMINISTRATION'),
        ('BOURBON','BOURBON'),
        ('CHAUDRONNERIE','CHAUDRONNERIE'),
        ('CHARPENTE MENUISERIE','CHARPENTE MENUISERIE'),
        ('COMPTABILITE FINANCE','COMPTABILITE FINANCE'),
        ('ELECTRICITE','ELECTRICITE'),
        ('G4S','G4S'),
        ('INFORMATIQUE ET TELECOM','INFORMATIQUE ET TELECOM'),
        ('IRIS','IRIS'),
        ('MAGASIN','MAGASIN'),
        ('MACHINE OUTILS','MACHINE OUTILS'),
        ('MAINTENANCE & TRAVAUX NEUFS','MAINTENANCE & TRAVAUX NEUFS'),
        ('MANUTENTION ET LEVAGE','MANUTENTION ET LEVAGE'),
        ('MECANIQUE BRD','MECANIQUE BRD'),
        ('NAVIRE','NAVIRE'),
        ('NETTOYAGE INDUSTRIEL','NETTOYAGE INDUSTRIEL'),
        ('PEINTURE','PEINTURE'),
        ('PEINTURE ANTICORROSION','PEINTURE ANTICORROSION'),
        ('PRODUCTION','PRODUCTION'),
        ('QUALITE ENVIRONNEMENT HYGIENE','QUALITE ENVIRONNEMENT HYGIENE'),
        ('QUALITE ENVIRONNEMENT HYGIENE ET SECURITE','QUALITE ENVIRONNEMENT HYGIENE ET SECURITE'),
        ('QHSE','QHSE'),
        ('RESSOURCES HUMAINES','RESSOURCES HUMAINES'),
        ('SAUVETAGE','SAUVETAGE'),
        ('SUPPLY CHAIN','SUPPLY CHAIN'),
        ('TUYAUTERIE','TUYAUTERIE'),
        ('WICS','WICS'),
    )

    date_consultation = models.DateField(auto_now_add=True)
    societe = models.CharField(max_length=50, choices=societes)
    matricule = models.CharField(unique=True, max_length=50)
    nom_prenoms = models.CharField(max_length=200)
    emploi_occupe = models.CharField(max_length=100, blank=True)
    atelier = models.CharField(max_length=100, choices=departement)
    type_visite = models.CharField(max_length=100, choices=visite)
    age = models.PositiveIntegerField(blank=True)
    affection_connue = models.CharField(max_length=15, choices=affection)
    nouvelle_affection = models.CharField(max_length=100)
    observation = models.TextField(blank=True)
    aptitude = models.CharField(max_length=100, choices=aptitudes)

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

    societes = (
        ('AGENT DE BORD','AGENT DE BORD'),
        ('CARENA','CARENA'),
        ('PRESTATAIRE','PRESTATAIRE'),
        ('REGIE','REGIE'),
    )

    departement = (
        ('ADMINISTRATION','ADMINISTRATION'),
        ('BOURBON','BOURBON'),
        ('CHAUDRONNERIE','CHAUDRONNERIE'),
        ('CHARPENTE MENUISERIE','CHARPENTE MENUISERIE'),
        ('COMPTABILITE FINANCE','COMPTABILITE FINANCE'),
        ('ELECTRICITE','ELECTRICITE'),
        ('G4S','G4S'),
        ('INFORMATIQUE ET TELECOM','INFORMATIQUE ET TELECOM'),
        ('IRIS','IRIS'),
        ('MAGASIN','MAGASIN'),
        ('MACHINE OUTILS','MACHINE OUTILS'),
        ('MAINTENANCE & TRAVAUX NEUFS','MAINTENANCE & TRAVAUX NEUFS'),
        ('MANUTENTION ET LEVAGE','MANUTENTION ET LEVAGE'),
        ('MECANIQUE BRD','MECANIQUE BRD'),
        ('NAVIRE','NAVIRE'),
        ('NETTOYAGE INDUSTRIEL','NETTOYAGE INDUSTRIEL'),
        ('PEINTURE','PEINTURE'),
        ('PEINTURE ANTICORROSION','PEINTURE ANTICORROSION'),
        ('PRODUCTION','PRODUCTION'),
        ('QUALITE ENVIRONNEMENT HYGIENE','QUALITE ENVIRONNEMENT HYGIENE'),
        ('QUALITE ENVIRONNEMENT HYGIENE ET SECURITE','QUALITE ENVIRONNEMENT HYGIENE ET SECURITE'),
        ('QHSE','QHSE'),
        ('RESSOURCES HUMAINES','RESSOURCES HUMAINES'),
        ('SAUVETAGE','SAUVETAGE'),
        ('SUPPLY CHAIN','SUPPLY CHAIN'),
        ('TUYAUTERIE','TUYAUTERIE'),
        ('WICS','WICS'),
    )

    date_consultation = models.DateField(auto_now_add=True)
    societe = models.CharField(max_length=50, choices=societes)
    matricule = models.CharField(unique=True, max_length=50)
    nom_prenoms = models.CharField(max_length=200)
    emploi_occupe = models.CharField(max_length=100, blank=True)
    atelier = models.CharField(max_length=100, choices=departement)
    type_visite = models.CharField(max_length=100, choices=visite)
    nature_risque = models.CharField(max_length=100, choices=risques, blank=True)
    age = models.PositiveIntegerField(blank=True)
    examen_realise = models.CharField(max_length=100, choices=examens, blank=True)
    affection_connue = models.CharField(max_length=15, choices=affection)
    nouvelle_affection = models.CharField(max_length=100)
    observation = models.TextField(blank=True)
    aptitude = models.CharField(max_length=100, choices=aptitudes)
    # travailleurs = models.ForeignKey(Travailleurs,on_delete= models.SET_NULL, null=True)

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

