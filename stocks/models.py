from django.db import models
from django.template.defaultfilters import slugify

from users.models import User

# Create your models here.
class Travailleurs(models.Model):
    choix = (
        ('CARENA','CARENA'),
        ('REGIE','REGIE'),
        ('PRESTATAIRE','PRESTATAIRE'),
        ('AGENT DE BORD','AGENT DE BORD'),
    )

    liste = (
        ('RMO','RMO'),
        ('SNS','SNS'),
        ('TMS','TMS'),
        ('MIRBAP','MIRBAP'),
        ('CTMCI','CTMCI'),
        ('EKAR','EKAR'),
        ('ETS AF','ETS AF'),
        ('E.A.C.I','E.A.C.I'),
        ('WICS','WICS'),
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

    nom = models.CharField(max_length=200)#Contient le nom et les prénoms
    email = models.EmailField(max_length=200, blank=True)
    atelier = models.CharField(max_length=100, choices=departement)
    matricule = models.CharField(unique=True, max_length=50)
    societe = models.CharField(max_length=20, choices=choix)
    societe_regie = models.CharField(max_length=20, choices=liste, blank=True)
    
    class Meta:
        ordering = ["nom"]
        verbose_name_plural  = 'Travailleurs'

    @classmethod
    def search_by_name(cls, nom):
        return cls.objects.filter(nom__icontains=nom) 

    @classmethod
    def search_by_matricule(cls, matricule):
        return cls.objects.filter(matricule=matricule) 

    def __str__(self) :
        return f"{self.matricule} - {self.nom}"
    
class Fournisseurs(models.Model):
    nom = models.CharField(max_length=30)
    prenoms = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, blank=True)
    societe = models.CharField(max_length=100)
    matricule = models.CharField(unique=True, max_length=100,blank=False)

    class Meta:
        ordering = ["nom"]
        verbose_name_plural = 'Fournisseurs'

    @classmethod
    def search_by_name(cls, nom):
        return cls.objects.filter(nom__icontains=nom) 

    @classmethod
    def search_by_matricule(cls, matricule):
        return cls.objects.filter(matricule=matricule) 

    def __str__(self) :
        return self.societe

class Medicaments(models.Model):
    nom_medoc = models.CharField(max_length=100)
    nom_commercial = models.CharField(max_length=100, blank=True)
    quantité_stock = models.PositiveBigIntegerField()
    quantité_detail = models.PositiveBigIntegerField()
    unité = models.CharField(max_length=100, blank=True)
    code_medoc = models.CharField(max_length=50)
    date_creation = models.DateTimeField(auto_now_add=True)
    fournisseur = models.ForeignKey(Fournisseurs,on_delete= models.SET_NULL, null=True, blank=True)
    expiration = models.DateField()
    plaquette_par_boite = models.PositiveBigIntegerField()
    slug = models.SlugField(blank=True)

    class Meta:
        ordering = ["nom_medoc"]
        verbose_name_plural = 'Médicaments'

    def __str__(self) :
        return self.nom_medoc

    def save(self, *args, **kwargs) :
        if not self.slug:
            self.slug = slugify(self.nom_medoc)   
        return super().save(*args, **kwargs)
    
    @classmethod
    def search_by_date(cls, date):
        return cls.objects.filter(date_creation=date)

    @classmethod
    def search_by_month(cls, mois):
        return cls.objects.filter(date_creation__month=mois)

    @classmethod
    def search_by_year(cls, année):
        return cls.objects.filter(date_creation__year=année)

    @classmethod
    def search_by_name(cls, nom_medoc):
        return cls.objects.filter(nom_medoc__icontains=nom_medoc)

class Transactions(models.Model):
    ACHAT = 'Entrée'
    VENTE = 'Sortie'
    choix = [
        (ACHAT,'Entrée'),
        (VENTE,'Sortie'),
    ]
    type_transaction = models.CharField(max_length=20, choices=choix)
    quantite = models.PositiveBigIntegerField()
    quantite_plaq = models.PositiveBigIntegerField()
    date_transaction = models.DateTimeField(auto_now_add=True)
    medicaments = models.ForeignKey(Medicaments,on_delete= models.SET_NULL, null=True)
    travailleurs = models.ForeignKey(Travailleurs,on_delete= models.SET_NULL, null=True)
    fournisseur = models.ForeignKey(Fournisseurs,on_delete= models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
   
    class Meta:
        ordering = ["date_transaction"]
        verbose_name_plural = 'Transactions'

    @classmethod
    def search_by_name(cls, medicaments):
        return cls.objects.filter(medicaments__nom_medoc__icontains=medicaments) 
    
    @classmethod
    def search_by_date(cls, date):
        return cls.objects.filter(date_transaction__date=date)

    @classmethod
    def search_by_month(cls, mois):
        return cls.objects.filter(date_transaction__month=mois)

    @classmethod
    def search_by_year(cls, année):
        return cls.objects.filter(date_transaction__year=année)
    
    def get_travailleurs(self):
        if self.travailleurs:
            return self.travailleurs
        else:
            return "Aucun"

    def get_fournisseur(self):
        if self.fournisseur:
            return self.fournisseur
        else:
            return "Aucun"


    def save(self, *args, **kwargs):
        request = kwargs.pop('request', None)  # Récupère l'objet request s'il existe
        self.user = request.user if request else None  # Assigne l'utilisateur connecté ou None
        super().save(*args, **kwargs)
