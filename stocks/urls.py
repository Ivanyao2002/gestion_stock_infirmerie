from django.urls import path
from .views import HomeMedocView,CreateMedocView, UpdateMedocView,TransactionView, HomeTransactionView, achat, vente,RechercheView, exporter_liste_medicaments, HomeFournView, HomeWorkView, CreateWorkerView, CreateFournView, export_transactions, expoter, export_etat, statistiques_details, statistiques_global

app_name = 'stocks'

urlpatterns = [
    path('medicines_list/', HomeMedocView.as_view(), name='list_medocs'),
    path('register_a_new_medicine/', CreateMedocView.as_view(), name='create_medocs'),
    path('update_medicine_<str:slug>/', UpdateMedocView.as_view(), name='update_medocs'),
    path('transaction/make_a_transaction/add/', RechercheView.as_view(), name='create_transaction'),
    path('transaction/transactions_list/', HomeTransactionView.as_view(), name='list_transaction'),
    path('transaction/make_a_transaction/remove/', TransactionView.as_view(), name='retrait_transaction'),
    path('transaction/make_a_transaction/<str:slug>/addition/', achat, name='ajouter'),
    path('transaction/make_a_transaction/<str:slug>/retraction/', vente, name='retirer'),
    path('export_to_excel/', exporter_liste_medicaments, name='export'),
    path('suppliers/suppliers_list/',HomeFournView.as_view(),name='list_fournisseur'),
    path('suppliers/add_a_new_supplier/',CreateFournView.as_view(),name='create_fournisseur'),
    path('workers/workers_list/',HomeWorkView.as_view(),name='list_worker'),
    path('workers/add_a_new_worker/',CreateWorkerView.as_view(),name='create_worker'),
    path('transactions/export_to_excel/', export_transactions, name='export_transactions'), 
    path('transactions/export_file_to_excel/', expoter, name='exporter'), 
    path('transactions/export_etat_to_excel/', export_etat, name='exporter_etat'),
    path('global_statistics/', statistiques_details, name='statistiques_detail' ),
    path('statistics/', statistiques_global, name='statistiques_global' ),

]