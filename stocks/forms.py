from django import forms
from .models import Medicaments, Transactions, Travailleurs, Fournisseurs


class MedicamentsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nom_medoc'].widget.attrs.update({
            'type':"text",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"floatingInput",
            'placeholder':"Paracétamol",
        })

        self.fields['nom_commercial'].widget.attrs.update({
            'type':"text",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"floatingInput",
            'placeholder':"Paracétamol",
        })

        self.fields['quantité_stock'].widget.attrs.update({
            'type':"text",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"floatingInput",
            'placeholder':"10",
        })

        self.fields['fournisseur'].widget.attrs.update({
            'type':"text",
            'class':"form-select",
            'style':"color: #DC143C;",
            'id':"floatingInput",
            'placeholder':"",
        })

        # self.fields['dosage'].widget.attrs.update({
        #     'type':"text",
        #     'class':"form-control ",
        #     'style':"color: #DC143C;",
        #     'id':"floatingInput",
        #     'placeholder':"2 fois par jours",
        # })

        self.fields['quantité_detail'].widget.attrs.update({
            'type':"text",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"floatingInput",
            'placeholder':"10",
        })

        # self.fields['date_expi'].widget.attrs.update({
        #     'type':"date",
        #     'class':"form-select ",
        #     'style':"color: #DC143C;",
        #     'id':"floatingInput",
        #     'placeholder':"",
        # })

        self.fields['code_medoc'].widget.attrs.update({
            'type':"text",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"floatingInput",
            'placeholder':"10",
        })

        self.fields['unité'].widget.attrs.update({
            'type':"text",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"floatingInput",
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
            'id':"floatingInput",
            'placeholder':"",
        })

        self.fields['type_transaction'].widget.attrs.update({
            'type':"text",
            'class':"form-select ",
            'style':"color: #DC143C;",
            'id':"floatingInput",
            'placeholder':"",
        })

        # self.fields['date_transaction'].widget.attrs.update({
        #     'type':"date",
        #     'class':"form-select ",
        #     'style':"color: #DC143C;",
        #     'id':"floatingInput",
        #     'placeholder':"",
            
        # })

        self.fields['quantite'].widget.attrs.update({
            'type':"text",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"floatingInput",
            'placeholder':"10",
        })

        self.fields['travailleurs'].widget.attrs.update({
            'type':"text",
            'class':"form-select",
            'style':"color: #DC143C;",
            'id':"floatingInput",
            'placeholder':"10",
        })

        self.fields['quantité_detail'].widget.attrs.update({
            'type':"text",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"floatingInput",
            'placeholder':"10",
        })

        self.fields['fournisseur'].widget.attrs.update({
            'type':"text",
            'class':"form-select",
            'style':"color: #DC143C;",
            'id':"floatingInput",
            'placeholder':"",
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
            'id':"floatingInput",
            'placeholder':"Paracétamol",
        })

        self.fields['societe_regie'].widget.attrs.update({
            'type':"text",
            'class':"form-select ",
            'style':"color: #DC143C;",
            'id':"floatingInput",
            'placeholder':"",
        })

        self.fields['email'].widget.attrs.update({
            'type':"text",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"floatingInput",
            'placeholder':"Paracétamol",
        })

        self.fields['atelier'].widget.attrs.update({
            'type':"text",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"floatingInput",
            'placeholder':"Paracétamol",
        })

        self.fields['matricule'].widget.attrs.update({
            'type':"text",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"floatingInput",
            'placeholder':"Paracétamol",
        })

        self.fields['societe'].widget.attrs.update({
            'type':"text",
            'class':"form-select ",
            'style':"color: #DC143C;",
            'id':"floatingInput",
            'placeholder':"",
        })        

    class Meta:
        model = Travailleurs
        exclude = ("slug",)

        # widgets = {
        #     'date_expi': forms.SelectDateWidget(years=range(2023,2050)),

        # }


class FournisseursForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nom'].widget.attrs.update({
            'type':"text",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"floatingInput",
            'placeholder':"Paracétamol",
        })

        self.fields['prenoms'].widget.attrs.update({
            'type':"text",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"floatingInput",
            'placeholder':"Paracétamol",
        })

        self.fields['matricule'].widget.attrs.update({
            'type':"text",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"floatingInput",
            'placeholder':"Paracétamol",
        })

        self.fields['societe'].widget.attrs.update({
            'type':"text",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"floatingInput",
            'placeholder':"Paracétamol",
        })

        self.fields['email'].widget.attrs.update({
            'type':"text",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"floatingInput",
            'placeholder':"Paracétamol",
        })

        # self.fields['unité'].widget.attrs.update({
        #     'type':"text",
        #     'class':"form-control ",
        #     'style':"color: #DC143C;",
        #     'id':"floatingInput",
        #     'placeholder':"10",
        # })

    class Meta:
        model = Fournisseurs
        exclude = ("slug",)

        # widgets = {
        #     'date_expi': forms.SelectDateWidget(years=range(2023,2050)),

        # }
      