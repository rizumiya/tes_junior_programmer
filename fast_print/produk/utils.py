from kategori.models import Kategori
from status.models import Status


def get_or_create_kategori(nama_kategori) -> Kategori:
    kategori, _ = Kategori.objects.get_or_create(nama_kategori=nama_kategori)
    return kategori


def get_or_create_status(nama_status) -> Status:
    status, _ = Status.objects.get_or_create(nama_status=nama_status)
    return status

