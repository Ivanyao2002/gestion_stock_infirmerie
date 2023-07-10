# Generated by Django 4.2.2 on 2023-07-10 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultation', '0005_delete_consultation_vma'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consultation_VMA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_consultation', models.DateField()),
                ('societe', models.CharField(choices=[('AGENT DE BORD', 'AGENT DE BORD'), ('CARENA', 'CARENA'), ('PRESTATAIRE', 'PRESTATAIRE'), ('REGIE', 'REGIE')], max_length=50)),
                ('matricule', models.CharField(max_length=50, unique=True)),
                ('nom_prenoms', models.CharField(max_length=200)),
                ('emploi_occupe', models.CharField(blank=True, max_length=100)),
                ('atelier', models.CharField(choices=[('ADMINISTRATION', 'ADMINISTRATION'), ('BOURBON', 'BOURBON'), ('CHAUDRONNERIE', 'CHAUDRONNERIE'), ('CHARPENTE MENUISERIE', 'CHARPENTE MENUISERIE'), ('COMPTABILITE FINANCE', 'COMPTABILITE FINANCE'), ('ELECTRICITE', 'ELECTRICITE'), ('G4S', 'G4S'), ('INFORMATIQUE ET TELECOM', 'INFORMATIQUE ET TELECOM'), ('IRIS', 'IRIS'), ('MAGASIN', 'MAGASIN'), ('MACHINE OUTILS', 'MACHINE OUTILS'), ('MAINTENANCE & TRAVAUX NEUFS', 'MAINTENANCE & TRAVAUX NEUFS'), ('MANUTENTION ET LEVAGE', 'MANUTENTION ET LEVAGE'), ('MECANIQUE BRD', 'MECANIQUE BRD'), ('NAVIRE', 'NAVIRE'), ('NETTOYAGE INDUSTRIEL', 'NETTOYAGE INDUSTRIEL'), ('PEINTURE', 'PEINTURE'), ('PEINTURE ANTICORROSION', 'PEINTURE ANTICORROSION'), ('PRODUCTION', 'PRODUCTION'), ('QUALITE ENVIRONNEMENT HYGIENE', 'QUALITE ENVIRONNEMENT HYGIENE'), ('QUALITE ENVIRONNEMENT HYGIENE ET SECURITE', 'QUALITE ENVIRONNEMENT HYGIENE ET SECURITE'), ('QHSE', 'QHSE'), ('RESSOURCES HUMAINES', 'RESSOURCES HUMAINES'), ('SAUVETAGE', 'SAUVETAGE'), ('SUPPLY CHAIN', 'SUPPLY CHAIN'), ('TUYAUTERIE', 'TUYAUTERIE'), ('WICS', 'WICS')], max_length=100)),
                ('type_visite', models.CharField(choices=[('VM ANNUELLE', 'VM ANNUELLE'), ('VM SPECIFIQUE', 'VM SPECIFIQUE')], max_length=100)),
                ('nature_risque', models.CharField(blank=True, choices=[('NUISANCE SONORE', 'NUISANCE SONORE'), ('RISQUES LIES AUX FUMEES ET VAPEURS TOXIQUES', 'RISQUES LIES AUX FUMEES ET VAPEURS TOXIQUES'), ('RISQUES LIES AUX POUSSIERES DE BOIS', 'RISQUES LIES AUX POUSSIERES DE BOIS'), ('RISQUES LIES AUX POUSSIERES DE SABLE', 'RISQUES LIES AUX POUSSIERES DE SABLE'), ('RISQUE LIE AUX PEINTURES (DILUANT, SOLVANTS) ET VERNIS', 'RISQUE LIE AUX PEINTURES (DILUANT, SOLVANTS) ET VERNIS'), ('RISQUES LIES AUX EMANATIONS DE DEBRIS DE METAUX', 'RISQUES LIES AUX EMANATIONS DE DEBRIS DE METAUX'), ('RISQUES LIES A LA PLONGEE (PROFONDEUR MOINS DE 15 METRES)', 'RISQUES LIES A LA PLONGEE (PROFONDEUR MOINS DE 15 METRES)'), ('RISQUES LIES AUX HUILES USAGEES ET DEGRAISSANTS (SOLVANTS)', 'RISQUES LIES AUX HUILES USAGEES ET DEGRAISSANTS (SOLVANTS)')], max_length=100)),
                ('age', models.PositiveIntegerField(blank=True)),
                ('examen_realise', models.CharField(blank=True, choices=[('AUDIOMETRIE', 'AUDIOMETRIE'), ('BIOLOGIE(NFS, TRANSA, CREAT, AUTRES)', 'BIOLOGIE(NFS, TRANSA, CREAT, AUTRES)'), ('EXAMEN CLINIQUE', 'EXAMEN CLINIQUE'), ('OPHTALMOLOGIE(AV, FO, VC, VR)', 'OPHTALMOLOGIE(AV, FO, VC, VR)'), ('RADIOLOGIE(PULMONAIRE, BLONDEAU)', 'RADIOLOGIE(PULMONAIRE, BLONDEAU)'), ('SPIROMETRIE', 'SPIROMETRIE')], max_length=100)),
                ('affection_connue', models.CharField(choices=[('CARDIO', 'CARDIO'), ('DERMATO', 'DERMATO'), ('DIGESTIVE', 'DIGESTIVE'), ('ENDOCRINIENNE', 'ENDOCRINIENNE'), ('HEMATO', 'HEMATO'), ('NEPHRO', 'NEPHRO'), ('NEURO', 'NEURO'), ('OPHTALMO', 'OPHTALMO'), ('ORL', 'ORL'), ('PNEUMO', 'PNEUMO'), ('RHUMATO', 'RHUMATO'), ('TRAUMATO', 'TRAUMATO'), ('UROLOGIQUE', 'UROLOGIQUE'), ('AUTRES', 'AUTRES')], max_length=15)),
                ('nouvelle_affection', models.CharField(max_length=100)),
                ('observation', models.TextField(blank=True)),
                ('aptitude', models.CharField(choices=[('APTE', 'APTE'), ('APTE : AVEC AMENAGEMENT', 'APTE : AVEC AMENAGEMENT'), ('INAPTE : DEFINITIF', 'INAPTE : DEFINITIF'), ('INAPTE : TEMPORAIRE', 'INAPTE : TEMPORAIRE'), ('INAPTE: AU POSTE MAIS APTE A UN AUTRE POSTE', 'INAPTE: AU POSTE MAIS APTE A UN AUTRE POSTE')], max_length=100)),
            ],
            options={
                'ordering': ['nom_prenoms'],
            },
        ),
    ]
