# Generated by Django 4.2.2 on 2023-08-01 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultations', '0013_alter_day_consultation_stop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day_consultation',
            name='stop',
            field=models.CharField(blank=True, choices=[('Avec arret', 'Avec arrêt'), ('Sans arret', 'Sans arrêt')], max_length=50),
        ),
    ]
