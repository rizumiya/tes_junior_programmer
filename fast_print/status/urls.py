from django.urls import path

from . import views

urlpatterns = [
    path('', views.tampilan_status, name='status'),
    path('update/<int:id_status>', views.tampilan_update_status, name='ubah_status'),
    path('delete/<int:id_status>', views.hapus_status, name='hapus_status'),
]