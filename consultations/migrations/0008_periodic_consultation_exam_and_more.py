# Generated by Django 4.2.2 on 2023-07-25 23:07

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('consultations', '0007_remove_periodic_consultation_exam_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='periodic_consultation',
            name='exam',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Audiometrie', 'Audiometrie'), ('Examen ophtalmologique', 'Examen ophtalmologique'), ('NFS, glycenie, proteinurie, glucosurie', 'NFS, glycénie, protéinurie, glucosurie'), ('Numeration formule sanguine', 'Numération formule sanguine'), ('Radiographie des sinus-blondeau', 'Radiographie des sinus-blondeau'), ('Radiographie pulmonaire', 'Radiographie pulmonaire'), ('Spirometrie', 'Spirométrie'), ('Transaminases, uree et creatine', 'Transaminases, urée et créatine'), ('Autres', 'Autres')], default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='periodic_consultation',
            name='risks',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Nuisance Sonore', 'Nuisance Sonore'), ('Risques lies aux Fumees et Vapeurs Toxiques', 'Risques liés aux fumées et vapeurs toxiques'), ('Risques lies aux poussieres de bois', 'Risques liés aux poussières de bois'), ('Risques lies aux poussieres de sable', 'Risques liés aux poussières de sable'), ('Risques lies aux peintures (diluants, solvants) et vernis', 'Risques liés aux peintures (diluants, solvants) et vernis'), ('Risques lies aux emanations de debris de metaux', 'Risques liés aux émanations de débris de métaux'), ('Risques lies a la plongee (profondeur moins de 15 metres)', 'Risques liés a la plongée (profondeur moins de 15 mètres)'), ('Risques lies aux huiles usagees et degraissants (solvants)', 'Risques liés aux huiles usagées et dégraissants (solvants)')], default='', max_length=100),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='periodic_consultation',
            name='pathology',
        ),
        migrations.AddField(
            model_name='periodic_consultation',
            name='pathology',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Cardiologie', 'Cardiologie'), ('Dermatologie', 'Dermatologie'), ('Digestive', 'Digestive'), ('Endocrinienne', 'Endocrinienne'), ('Endocrinologie', 'Endocrinologie'), ('Gastro-enterologie', 'Gastro-entérologie'), ('Gynecologie', 'Gynécologie'), ('Hematologie', 'Hématologie'), ('Maladies Infectieuses', 'Maladies Infectieuses'), ('Nephrologie', 'Néphrologie'), ('Neurologie', 'Neurologie'), ('ORL', 'ORL'), ('Ophtalmologie', 'Ophtalmologie'), ('Pneumologie', 'Pneumologie'), ('Psychiatrie', 'Psychiatrie'), ('Rhumatologie', 'Rhumatologie'), ('Stomatologie', 'Stomatologie'), ('Traumatologie', 'Traumatologie'), ('Urologie', 'Urologie'), ('Autres', 'Autres')], default='', max_length=100),
            preserve_default=False,
        ),
    ]
