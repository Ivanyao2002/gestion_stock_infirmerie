# Generated by Django 4.2.2 on 2023-08-17 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultations', '0018_day_consultation_prescription_day_consultation_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day_consultation',
            name='prescription',
            field=models.TextField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='periodic_consultation',
            name='prescription',
            field=models.TextField(blank=True, default='', max_length=200),
        ),
    ]
