from django import forms

from .models import Periodic_Consultation, Day_Consultation


class PeriodicConsultationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['observations'].widget.attrs.update({
            'type':"text",
            'class':"form-control",
            'style':"color: #DC143C; height: 80px;",
            'id':"observations",
            'placeholder':"observations",
        })

        self.fields['reasons'].widget.attrs.update({
            'type':"text",
            'class':"form-select ",
            'style':"color: #DC143C;",
            'id':"reasons",
            'placeholder':"motif de visite",
        })

        self.fields['aptitude'].widget.attrs.update({
            'type':"text",
            'class':"form-select ",
            'style':"color: #DC143C;",
            'id':"aptitude",
            'placeholder':"aptitude",
        })

        self.fields['other_pathology'].widget.attrs.update({
            'type':"text",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"other_pathology",
            'placeholder':"autre pathologie",
        })

        self.fields['other_exam'].widget.attrs.update({
            'type':"text",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"other_exam",
            'placeholder':"autre examen",
        })

        self.fields['break_day'].widget.attrs.update({
            'type':"number",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"break_day",
            'placeholder':"jour de congés",
        })

        self.fields['evacuation'].widget.attrs.update({
            'type':"checkbox",
            'class':"form-check-input",
            'style':"color: #DC143C;",
            'id':"evacuation",
            'placeholder':"evacuation",
        })

        self.fields['matricule'].widget.attrs.update({
            'type':"text",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"matricule",
            'placeholder':"matricule",
        })

        self.fields['nom_prenoms'].widget.attrs.update({
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"nom_prenoms",
            'placeholder':"nom prenoms",
            'readonly':True,
        })

        self.fields['societe'].widget.attrs.update({
            'class':"form-select ",
            'style':"color: #DC143C;",
            'id':"societe",
            'placeholder':"societe",
        })

        self.fields['atelier'].widget.attrs.update({
            'class':"form-select ",
            'style':"color: #DC143C;",
            'id':"atelier",
            'placeholder':"atelier",
            # 'disabled':True,
        })

    #####VALIDATION, AFFICHAGE D ERREUR 
        self.fields['matricule'].error_messages = {
            'unique': "Ce matricule existe déjà. Veuillez en choisir un autre, chaque matricule est unique.",
            'required': "Le champ 'Matricule' est obligatoire.",
        }
        self.fields['reasons'].error_messages = {
            'required': "Le champ 'Motif de visite' est obligatoire.",
        }
        self.fields['aptitude'].error_messages = {
            'required': "Le champ 'Aptitude' est obligatoire.",
        }

    class Meta:
        model = Periodic_Consultation
        fields = '__all__'
        widgets = {
            'risks': forms.SelectMultiple(
                attrs={'class': 'form-control select2', 
                        'style': 'color: #DC143C;', 
                        'id': 'risks', 
                    }),
            'pathology': forms.SelectMultiple(
                attrs={'class': 'form-control select2', 
                        'style': 'color: #DC143C;', 
                        'id': 'pathology', 
                    }),
            'exam': forms.SelectMultiple(
                attrs={'class': 'form-control select2', 
                        'style': 'color: #DC143C;', 
                        'id': 'exam', 
                    }), 
        } 


class DayConsultationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['observations'].widget.attrs.update({
            'type':"text",
            'class':"form-control",
            'style':"color: #DC143C;",
            'id':"observations",
            'placeholder':"observations",
        })

        self.fields['stop'].widget.attrs.update({
            'type':"text",
            'class':"form-select ",
            'style':"color: #DC143C;",
            'id':"stop",
            'placeholder':"accident",
        })

        self.fields['accident'].widget.attrs.update({
            'type':"text",
            'class':"form-select ",
            'style':"color: #DC143C;",
            'id':"accident",
            'placeholder':"accident",
        })

        self.fields['siege'].widget.attrs.update({
            'type':"text",
            'class':"form-select ",
            'style':"color: #DC143C;",
            'id':"siege",
            'placeholder':"siege",
        })

        self.fields['lesion'].widget.attrs.update({
            'type':"text",
            'class':"form-select ",
            'style':"color: #DC143C;",
            'id':"lesion",
            'placeholder':"lesion",
        })        

        self.fields['reasons'].widget.attrs.update({
            'type':"text",
            'class':"form-select ",
            'style':"color: #DC143C;",
            'id':"reasons",
            'placeholder':"motif de visite",
        })

        self.fields['aptitude'].widget.attrs.update({
            'type':"text",
            'class':"form-select ",
            'style':"color: #DC143C;",
            'id':"aptitude",
            'placeholder':"aptitude",
        })

        self.fields['other_pathology'].widget.attrs.update({
            'type':"text",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"other_pathology",
            'placeholder':"autre pathologie",
        })

        self.fields['other_siege'].widget.attrs.update({
            'type':"text",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"other_siege",
            'placeholder':"autre siege",
        })

        self.fields['other_lesion'].widget.attrs.update({
            'type':"text",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"other_lesion",
            'placeholder':"autre lesion",
        })

        self.fields['break_day'].widget.attrs.update({
            'type':"number",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"break_day",
            'placeholder':"jour de congés",
        })

        self.fields['evacuation'].widget.attrs.update({
            'type':"checkbox",
            'class':"form-check-input",
            'style':"color: #DC143C;",
            'id':"evacuation",
            'placeholder':"evacuation",
        })

        self.fields['matricule'].widget.attrs.update({
            'type':"text",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"matricule",
            'placeholder':"matricule",
        })

        self.fields['nom_prenoms'].widget.attrs.update({
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"nom_prenoms",
            'placeholder':"nom prenoms",
            'readonly':True,
        })

        self.fields['societe'].widget.attrs.update({
            'class':"form-select ",
            'style':"color: #DC143C;",
            'id':"societe",
            'placeholder':"societe",
        })

        self.fields['atelier'].widget.attrs.update({
            'class':"form-select ",
            'style':"color: #DC143C;",
            'id':"atelier",
            'placeholder':"atelier",
        })
 
     #####VALIDATION, AFFICHAGE D ERREUR 
        self.fields['matricule'].error_messages = {
            'unique': "Ce matricule existe déjà. Veuillez en choisir un autre, chaque matricule est unique.",
            'required': "Le champ 'Matricule' est obligatoire.",
        }
        self.fields['reasons'].error_messages = {
            'required': "Le champ 'Motif de visite' est obligatoire.",
        }
        self.fields['aptitude'].error_messages = {
            'required': "Le champ 'Aptitude' est obligatoire.",
        }
        self.fields['stop'].error_messages = {
            'required': "Le champ 'stop' est obligatoire.",
        }
 
    class Meta:
        model = Day_Consultation
        fields = '__all__'
        widgets = {
            'pathology': forms.SelectMultiple(
                attrs={'class': 'form-control select2', 
                        'style': 'color: #DC143C;', 
                        'id': 'pathology', 
                    }),
        } 

class CongeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['break_day'].widget.attrs.update({
            'type':"number",
            'class':"form-control ",
            'style':"color: #DC143C;",
            'id':"break_day",
            'placeholder':"jour de congés",
        })

        self.fields['evacuation'].widget.attrs.update({
            'type':"checkbox",
            'class':"form-check-input",
            'style':"color: #DC143C;",
            'id':"evacuation",
            'placeholder':"evacuation",
        })

    class Meta:
        model = Day_Consultation
        fields = ("break_day","evacuation")


