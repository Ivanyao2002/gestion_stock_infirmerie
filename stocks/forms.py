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
            'type':"text",
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
            'type':"text",
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
            'type':"text",
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
            'type':"text",
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
            'placeholder':"Paracétamol",
        })

        self.fields['societe_regie'].widget.attrs.update({
            'type':"text",
            'class':"form-select ",
            'style':"color: #DC143C;",
            'id':"societe_regie",
            'placeholder':"",
        })

        self.fields['email'].widget.attrs.update({
            'type':"text",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"email",
            'placeholder':"Paracétamol",
        })

        self.fields['atelier'].widget.attrs.update({
            'type':"text",
            'class':"form-select ",
            'style':"color: #DC143C;",
            'id':"atelier",
            'placeholder':"Paracétamol",
        })

        self.fields['matricule'].widget.attrs.update({
            'type':"text",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"matricule",
            'placeholder':"Paracétamol",
        })

        self.fields['societe'].widget.attrs.update({
            'type':"text",
            'class':"form-select ",
            'style':"color: #DC143C;",
            'id':"societe",
            'placeholder':"",
        })        

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
            'placeholder':"Paracétamol",
        })

        self.fields['prenoms'].widget.attrs.update({
            'type':"text",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"prenoms",
            'placeholder':"Paracétamol",
        })

        self.fields['matricule'].widget.attrs.update({
            'type':"text",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"matricule",
            'placeholder':"Paracétamol",
        })

        self.fields['societe'].widget.attrs.update({
            'type':"text",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"societe",
            'placeholder':"Paracétamol",
        })

        self.fields['email'].widget.attrs.update({
            'type':"text",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"email",
            'placeholder':"Paracétamol",
        })

    class Meta:
        model = Fournisseurs
        exclude = ("slug",)