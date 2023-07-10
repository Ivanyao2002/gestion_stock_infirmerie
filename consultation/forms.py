from django import forms
from .models import Consultation_journaliere, Consultation_VMA


class Consultation_VmaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nom_prenoms'].widget.attrs.update({
            'type':"text",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"floatingInput",
            'placeholder':"nom_prenoms",
        })

        self.fields['societe'].widget.attrs.update({
            'type':"text",
            'class':"form-select ",
            'style':"color: #DC143C;",
            'id':"floatingInput",
            'placeholder':"societe",
        })

        self.fields['matricule'].widget.attrs.update({
            'type':"text",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"floatingInput",
            'placeholder':"matricule",
        })

        self.fields['emploi_occupe'].widget.attrs.update({
            'type':"text",
            'class':"form-control",
            'style':"color: #DC143C;",
            'id':"floatingInput",
            'placeholder':"emploi_occupe",
        })

        self.fields['atelier'].widget.attrs.update({
            'type':"text",
            'class':"form-select ",
            'style':"color: #DC143C;",
            'id':"floatingInput",
            'placeholder':"atelier",
        })

        self.fields['type_visite'].widget.attrs.update({
            'type':"text",
            'class':"form-select ",
            'style':"color: #DC143C;",
            'id':"floatingInput",
            'placeholder':"type_visite",
        })

        self.fields['age'].widget.attrs.update({
            'type':"integer",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"floatingInput",
            'placeholder':"age",
        })

        self.fields['affection_connue'].widget.attrs.update({
            'type':"text",
            'class':"form-select ",
            'style':"color: #DC143C;",
            'id':"floatingInput",
            'placeholder':"affection_connue",
        })

        self.fields['nouvelle_affection'].widget.attrs.update({
            'type':"text",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"floatingInput",
            'placeholder':"nouvelle_affection",
        })

        self.fields['observation'].widget.attrs.update({
            'type':"text",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"floatingInput",
            'placeholder':"observation",
        })

        self.fields['aptitude'].widget.attrs.update({
            'type':"text",
            'class':"form-select ",
            'style':"color: #DC143C;",
            'id':"floatingInput",
            'placeholder':"aptitude",
        })

        self.fields['examen_realise'].widget.attrs.update({
            'type':"text",
            'class':"form-select ",
            'style':"color: #DC143C;",
            'id':"floatingInput",
            'placeholder':"examen_realise",
        })

        self.fields['nature_risque'].widget.attrs.update({
            'type':"text",
            'class':"form-select ",
            'style':"color: #DC143C;",
            'id':"floatingInput",
            'placeholder':"nature_risque",
        })
   
    class Meta:
        model = Consultation_VMA
        exclude = ("slug",)


class Consultation_JourForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nom_prenoms'].widget.attrs.update({
            'type':"text",
            'class':"form-control",
            'style':"color: #DC143C;",
            'id':"floatingInput",
            'placeholder':"Nom",
        })

        self.fields['societe'].widget.attrs.update({
            'type':"text",
            'class':"form-select ",
            'style':"color: #DC143C;",
            'id':"floatingInput",
            'placeholder':"societe",
        })

        self.fields['matricule'].widget.attrs.update({
            'type':"text",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"floatingInput",
            'placeholder':"matricule",
        })

        self.fields['emploi_occupe'].widget.attrs.update({
            'type':"text",
            'class':"form-control",
            'style':"color: #DC143C;",
            'id':"floatingInput",
            'placeholder':"emploi_occupe",
        })

        self.fields['atelier'].widget.attrs.update({
            'type':"text",
            'class':"form-select ",
            'style':"color: #DC143C;",
            'id':"floatingInput",
            'placeholder':"atelier",
        })

        self.fields['type_visite'].widget.attrs.update({
            'type':"text",
            'class':"form-select ",
            'style':"color: #DC143C;",
            'id':"floatingInput",
            'placeholder':"type_visite",
        })

        self.fields['age'].widget.attrs.update({
            'type':"integer",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"floatingInput",
            'placeholder':"age",
        })

        self.fields['affection_connue'].widget.attrs.update({
            'type':"text",
            'class':"form-select ",
            'style':"color: #DC143C;",
            'id':"floatingInput",
            'placeholder':"affection_connue",
        })

        self.fields['nouvelle_affection'].widget.attrs.update({
            'type':"text",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"floatingInput",
            'placeholder':"nouvelle_affection",
        })

        self.fields['observation'].widget.attrs.update({
            'type':"text",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"floatingInput",
            'placeholder':"observation",
        })

        self.fields['aptitude'].widget.attrs.update({
            'type':"text",
            'class':"form-select ",
            'style':"color: #DC143C;",
            'id':"floatingInput",
            'placeholder':"aptitude",
        })

    class Meta:
        model = Consultation_journaliere
        exclude = ("slug",)

