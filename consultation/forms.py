from django import forms
# from django.db.models import Q

from .models import Consultation_journaliere, Consultation_VMA
# from stocks.models import Travailleurs

# class TravailleursSelectWidget(forms.Select):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.attrs['class'] = 'select2'
    
#     # def get_context(self, name, value, attrs):
#     #     context = super().get_context(name, value, attrs)
#     #     travailleurs = Travailleurs.objects.all()

#     #     if value:
#     #         travailleurs = travailleurs.filter(
#     #             models.Q(matricule__icontains=value) | models.Q(nom__icontains=value)
#     #         )
        
#     #     context['widget']['value'] = value
#     #     context['widget']['travailleurs'] = travailleurs

#     #     return context

#     def get_context(self, name, value, attrs):
#         context = super().get_context(name, value, attrs)
#         travailleurs = Travailleurs.objects.all()

#         if value:
#             travailleurs = travailleurs.filter(
#                 Q(matricule__icontains=value) | Q(nom__icontains=value)
#             )
        
#         context['widget']['value'] = value
#         context['widget']['travailleurs'] = travailleurs

#         return context 


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
   
        self.fields['travailleurs'].widget.attrs.update({
            'type':"text",
            'class':"form-select ",
            'style':"color: #DC143C;",
            'id':"floatingInput",
            'placeholder':"travailleurs",
        })
    class Meta:
        model = Consultation_VMA
        exclude = ("slug",)


class Consultation_JourForm(forms.ModelForm):
    # travailleurs = forms.ModelChoiceField(queryset=Travailleurs.objects.all(), widget=TravailleursSelectWidget)
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

        self.fields['travailleurs'].widget.attrs.update({
            'type':"text",
            'class':"form-select ",
            'style':"color: #DC143C;",
            'id':"floatingInput",
            'placeholder':"travailleurs",
        })

    class Meta:
        model = Consultation_journaliere
        exclude = ("slug",)


