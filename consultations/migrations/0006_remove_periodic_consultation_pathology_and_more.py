# Generated by Django 4.2.2 on 2023-07-25 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultations', '0005_alter_day_consultation_break_day_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='periodic_consultation',
            name='pathology',
        ),
        migrations.AddField(
            model_name='periodic_consultation',
            name='pathology',
            field=models.ManyToManyField(to='consultations.periodic_consultation'),
        ),
    ]
