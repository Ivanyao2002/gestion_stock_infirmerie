# Generated by Django 4.2.2 on 2023-07-19 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0015_alter_medicaments_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicaments',
            name='seuil_alerte',
            field=models.PositiveIntegerField(blank=True, default=10),
        ),
    ]
