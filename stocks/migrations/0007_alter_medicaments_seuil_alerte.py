# Generated by Django 4.2.2 on 2023-06-20 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0006_notification_medicaments_seuil_alerte'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicaments',
            name='seuil_alerte',
            field=models.PositiveIntegerField(blank=True, default=10),
        ),
    ]
