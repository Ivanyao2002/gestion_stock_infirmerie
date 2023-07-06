from django.urls import path
from .views import HomeMedocView,CreateMedocView, UpdateMedocView, DeleteMedocView,TransactionView, HomeTransactionView, achat, vente,RechercheView, exporter_liste_medicaments, HomeFournView, HomeWorkView, CreateWorkerView, CreateFournView, export_transactions, expoter, export_etat, statistiques_details, statistiques_global, DeleteFournisseur, DeleteWorker


app_name = 'stocks'

urlpatterns = [
    path('liste-des-medicaments/', HomeMedocView.as_view(), name='list_medocs'),
    path('ajouter-un-medicament/', CreateMedocView.as_view(), name='create_medocs'),
    path('modifier-<str:slug>/', UpdateMedocView.as_view(), name='update_medocs'),
    path('supprimer-<str:slug>/', DeleteMedocView.as_view(), name='delete_medocs'),
    path('transaction/faire-une-transaction/ajouter/', RechercheView.as_view(), name='create_transaction'),
    path('transaction/liste-des-transactions/', HomeTransactionView.as_view(), name='list_transaction'),
    path('transaction/faire-une-transaction/retirer/', TransactionView.as_view(), name='retrait_transaction'),
    path('transaction/faire-une-transaction/<str:slug>/ajout/', achat, name='ajouter'),
    path('transaction/faire-une-transaction/<str:slug>/retrait/', vente, name='retirer'),
    path('expoter-en-excel/', exporter_liste_medicaments, name='export'),
    path('fournisseur/liste-des-fournisseurs/',HomeFournView.as_view(),name='list_fournisseur'),
    path('fournisseur/enregistrer-un-fournisseur/',CreateFournView.as_view(),name='create_fournisseur'),
    path('travailleurs/liste-des-travailleurs/',HomeWorkView.as_view(),name='list_worker'),
    path('travailleurs/enregistrer-un-travailleur/',CreateWorkerView.as_view(),name='create_worker'),
    path('transactions/exporter/', export_transactions, name='export_transactions'), 
    path('transactions/exporter-vers/', expoter, name='exporter'), 
    path('transactions/exporter-etat/', export_etat, name='exporter_etat'),
    path('statistiques/', statistiques_details, name='statistiques_detail' ),
    path('statistics/', statistiques_global, name='statistiques_global' ),
    path('worker/supprimer-travailleur-<int:pk>/', DeleteWorker.as_view(), name='delete_worker'),
    path('fournisseur/supprimer-fournisseur<int:pk>/', DeleteFournisseur.as_view(), name='delete_fournisseur'),
]