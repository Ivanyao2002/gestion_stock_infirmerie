# Generated by Django 4.2.1 on 2023-06-06 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicaments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_medoc', models.CharField(max_length=100)),
                ('nom_commercial', models.CharField(max_length=100)),
                ('quantité_stock', models.IntegerField()),
                ('unité', models.CharField(blank=True, max_length=100)),
                ('code_medoc', models.CharField(max_length=50)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True)),
            ],
            options={
                'ordering': ['date_creation'],
            },
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_transaction', models.CharField(choices=[('Entrée', 'Entrée'), ('Sortie', 'Sortie')], max_length=20)),
                ('quantite', models.IntegerField()),
                ('date_transaction', models.DateTimeField(auto_now_add=True)),
                ('medicaments', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stocks.medicaments')),
            ],
            options={
                'ordering': ['date_transaction'],
            },
        ),
    ]
