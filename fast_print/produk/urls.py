from django.urls import path

from . import views

urlpatterns = [
    path('', views.tampilan_produk, name='produk'),
    path('update/<int:id_produk>', views.tampilan_update_produk, name='ubah_produk'),
    path('delete/<int:id_produk>', views.hapus_produk, name='hapus_produk'),
]

