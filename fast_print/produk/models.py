from django.db import models

from kategori.models import Kategori
from status.models import Status


class Produk(models.Model):
    id_produk = models.BigAutoField(primary_key=True)
    nama_produk = models.CharField(max_length=120)
    harga = models.DecimalField(decimal_places=2, max_digits=10)
    kategori_id = models.ForeignKey(Kategori, on_delete=models.CASCADE, related_name='produk')
    status_id = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='produk')
