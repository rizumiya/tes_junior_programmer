from django.urls import path

from . import views

urlpatterns = [
    path('', views.tampilan_kategori, name='kategori'),
    path('update/<int:id_kategori>', views.tampilan_update_kategori, name='ubah_kategori'),
    path('delete/<int:id_kategori>', views.hapus_kategori, name='hapus_kategori'),
]