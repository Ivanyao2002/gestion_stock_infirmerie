# Generated by Django 4.2.2 on 2023-07-26 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultations', '0009_alter_day_consultation_accident_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day_consultation',
            name='stop',
            field=models.CharField(choices=[('Avec arret', 'Avec arrêt'), ('Sans arret', 'Sans arrêt')], default='', max_length=100),
        ),
    ]
