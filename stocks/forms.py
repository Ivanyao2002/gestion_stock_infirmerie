from django import forms
from .models import Medicaments, Transactions, Travailleurs, Fournisseurs


class MedicamentsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nom_medoc'].widget.attrs.update({
            'type':"text",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"nom_medoc",
            'placeholder':"Paracétamol",
        })

        self.fields['nom_commercial'].widget.attrs.update({
            'type':"text",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"nom_commercial",
            'placeholder':"Paracétamol",
        })

        self.fields['quantité_stock'].widget.attrs.update({
            'type':"number",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"quantité_stock",
            'placeholder':"10",
        })

        self.fields['fournisseur'].widget.attrs.update({
            'type':"text",
            'class':"form-select",
            'style':"color: #DC143C;",
            'id':"fournisseur",
            'placeholder':"fournisseur",
        })

        self.fields['quantité_detail'].widget.attrs.update({
            'type':"number",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"quantité_detail",
            'placeholder':"10",
        })

        self.fields['code_medoc'].widget.attrs.update({
            'type':"text",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"code_medoc",
            'placeholder':"10",
        })

        self.fields['unité'].widget.attrs.update({
            'type':"text",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"unité",
            'placeholder':"10",
        })

        self.fields['expiration'].widget.attrs.update({
            'type':"date",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"expiration",
            'placeholder':"date d'expiration",
        })

        self.fields['plaquette_par_boite'].widget.attrs.update({
            'type':"number",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"plaquette_par_boite",
            'placeholder':"plaquette par boite",
        })        
        

    class Meta:
        model = Medicaments
        exclude = ("slug",)

        widgets = {
            'date_expi': forms.SelectDateWidget(years=range(2023,2050)),
        }


class TransactionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['medicaments'].widget.attrs.update({
            'type':"text",
            'class':"form-select ",
            'style':"color: #DC143C;",
            'id':"medicaments",
            'placeholder':"medicaments",
        })

        self.fields['type_transaction'].widget.attrs.update({
            'type':"text",
            'class':"form-select ",
            'style':"color: #DC143C;",
            'id':"type_transaction",
            'placeholder':"type",
        })

        self.fields['quantite'].widget.attrs.update({
            'type':"number",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"quantite",
            'placeholder':"10",
        })

        self.fields['travailleurs'].widget.attrs.update({
            'type':"text",
            'class':"form-select",
            'style':"color: #DC143C;",
            'id':"travailleurs",
            'placeholder':"travailleur",
        })

        self.fields['quantité_detail'].widget.attrs.update({
            'type':"number",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"quantité_detail",
            'placeholder':"10",
        })

        self.fields['fournisseur'].widget.attrs.update({
            'type':"text",
            'class':"form-select",
            'style':"color: #DC143C;",
            'id':"fournisseur",
            'placeholder':"fournisseur",
        })

    class Meta:
        model = Transactions
        exclude = ("slug",)
        
class TravailleursForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nom'].widget.attrs.update({
            'type':"text",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"nom",
            'placeholder':"Nom et Prenoms",
            'pattern':"[A-Za-z\s]*",
            'name':"nom",
            'oninput':"filterNumericChars()", 
        })

        self.fields['societe_regie'].widget.attrs.update({
            'type':"text",
            'class':"form-select ",
            'style':"color: #DC143C;",
            'id':"societe_regie",
            'placeholder':"societe_regie",
        })

        self.fields['email'].widget.attrs.update({
            'type':"text",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"email",
            'placeholder':"email",
            'name':"email",
            'oninput':"validateEmail()", 
        })

        self.fields['atelier'].widget.attrs.update({
            'type':"text",
            'class':"form-select ",
            'style':"color: #DC143C;",
            'id':"atelier",
            'placeholder':"atelier",
        })

        self.fields['matricule'].widget.attrs.update({
            'type':"text",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"matricule",
            'placeholder':"matricule",
            'name':"matricule",
            'oninput':"filterNonNumericChars()", 
            'pattern':"[0-9]*",
        })

        self.fields['societe'].widget.attrs.update({
            'type':"text",
            'class':"form-select ",
            'style':"color: #DC143C;",
            'id':"societe",
            'placeholder':"societe",
        })        

     #####VALIDATION, AFFICHAGE D ERREUR 
        self.fields['matricule'].error_messages = {
            'unique': "Ce matricule existe déjà. Veuillez en choisir un autre, chaque matricule est unique.",
            'required': "Le champ 'Matricule' est obligatoire.",
        }
 

    class Meta:
        model = Travailleurs
        exclude = ("slug",)


class FournisseursForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nom'].widget.attrs.update({
            'type':"text",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"nom",
            'placeholder':"nom",
            'pattern':"[A-Za-z]*",
            'name':"nom",
            'oninput':"filtreNumericChars()",
        })

        self.fields['prenoms'].widget.attrs.update({
            'type':"text",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"prenoms",
            'placeholder':"penoms",
            'pattern':"[A-Za-z\s]*",
            'name':"nom",
            'oninput':"filterNumericChars()",
        })

        self.fields['matricule'].widget.attrs.update({
            'type':"text",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"matricule",
            'placeholder':"matricule",
            'name':"matricule",
            'oninput':"filterNonNumericChars()", 
            'pattern':"[0-9]*",
        })

        self.fields['societe'].widget.attrs.update({
            'type':"text",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"societe",
            'placeholder':"societe",
        })

        self.fields['email'].widget.attrs.update({
            'type':"text",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"email",
            'placeholder':"email",
            'name':"email",
            'oninput':"validateEmail()", 
        })

     #####VALIDATION, AFFICHAGE D ERREUR 
        self.fields['matricule'].error_messages = {
            'unique': "Ce matricule existe déjà. Veuillez en choisir un autre, chaque matricule est unique.",
            'required': "Le champ 'Matricule' est obligatoire.",
        }
 
    class Meta:
        model = Fournisseurs
        exclude = ("slug",)