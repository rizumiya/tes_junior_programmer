from django.db import models

class Kategori(models.Model):
    id_kategori = models.BigAutoField(primary_key=True)
    nama_kategori = models.CharField(max_length=100)

