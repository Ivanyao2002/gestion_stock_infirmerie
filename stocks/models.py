from django.db import models
from django.template.defaultfilters import slugify

from users.models import User

# Create your models here.
class Travailleurs(models.Model):
    choix = (
        ('CARENA','CARENA'),
        ('REGIE','REGIE'),
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

    nom = models.CharField(max_length=200,blank=False)#Contient le nom et les prénoms
    email = models.EmailField(max_length=200)
    atelier = models.CharField(max_length=100,blank=False)
    matricule = models.CharField(unique=True, max_length=50,blank=False)
    societe = models.CharField(max_length=20, choices=choix)
    societe_regie = models.CharField(max_length=20, choices=liste, blank=True)
    
    class Meta:
        ordering = ["nom"]

    def __str__(self) :
        return self.nom
    
class Fournisseurs(models.Model):
    nom = models.CharField(max_length=30,blank=False)
    prenoms = models.CharField(max_length=100,blank=False)
    email = models.EmailField(max_length=200)
    societe = models.CharField(max_length=100,blank=False)
    matricule = models.CharField(unique=True, max_length=100,blank=False)

    class Meta:
        ordering = ["nom"]

    def __str__(self) :
        return self.societe

class Medicaments(models.Model):
    nom_medoc = models.CharField(max_length=100)
    nom_commercial = models.CharField(max_length=100)
    # dosage = models.CharField(max_length=100, blank=True)
    # date_expi = models.DateField()
    quantité_stock = models.IntegerField()
    quantité_detail = models.IntegerField()
    unité = models.CharField(max_length=100, blank=True)
    code_medoc = models.CharField(max_length=50)
    date_creation = models.DateTimeField(auto_now_add=True)
    fournisseur = models.ForeignKey(Fournisseurs,on_delete= models.SET_NULL, null=True)
    seuil_alerte = models.PositiveIntegerField(default=10, blank=True)


    slug = models.SlugField(blank=True)

    class Meta:
        ordering = ["date_creation"]

    def __str__(self) :
        return self.nom_medoc

    def save(self, *args, **kwargs) :
        if not self.slug:
            self.slug = slugify(self.nom_medoc) 
        # if self.pk:
            # self.quantité_stock = self.quantité_detail // self.plaqte_par_boite     
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
    quantite = models.IntegerField()
    quantite_plaq = models.IntegerField()
    date_transaction = models.DateTimeField(auto_now_add=True)
    medicaments = models.ForeignKey(Medicaments,on_delete= models.SET_NULL, null=True)
    travailleurs = models.ForeignKey(Travailleurs,on_delete= models.SET_NULL, null=True)
    fournisseur = models.ForeignKey(Fournisseurs,on_delete= models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
   
    class Meta:
        ordering = ["date_transaction"]

    @classmethod
    def search_by_name(cls, medicaments):
        return cls.objects.filter(medicaments__nom_medoc__icontains=medicaments) 
    
    @classmethod
    def search_by_date(cls, date):
        return cls.objects.filter(date_transaction__date=date)
    # date_obj = datetime.strptime(date, '%Y-%m-%d').date()
        # return cls.objects.filter(date_transaction=date_obj)

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
