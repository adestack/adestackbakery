from django.contrib import admin
from django.urls import path, include

admin.autodiscover()

import disbursement.views

urlpatterns = [
    path('', disbursement.views.index, name='index'),
    path('balance', disbursement.views.balance, name='balance'),
    path('disbursements', disbursement.views.disbursements, name='disbursements'),
    path('suppliers', disbursement.views.suppliers, name='suppliers'),
    path('suppliers/add', disbursement.views.add_supplier, name='add_supplier'),
    path('suppliers/add_ajax', disbursement.views.add_supplier_ajax, name='add_supplier_ajax'),
    path('suppliers/edit/<int:id>/', disbursement.views.edit_supplier, name='edit_supplier'),
    path('suppliers/delete/<int:id>/', disbursement.views.delete_supplier, name='delete_supplier'),
    path('disbursements/single', disbursement.views.single_disbursement, name='single_disbursement'),
    path('disbursements/single_ajax', disbursement.views.single_disbursement_ajax, name='single_disbursement_ajax'),
    path('disbursements/bulk', disbursement.views.bulk_disbursements, name='bulk_disbursements'),
    path('admin/', admin.site.urls),
]
