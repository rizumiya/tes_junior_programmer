import json
import hashlib
import datetime

from kategori.models import Kategori
from status.models import Status


NOW = datetime.datetime.now()
WITA = NOW + datetime.timedelta(hours=1)

def get_username(base_name: str) -> str : 
    """Membuat username untuk API"""
    tgl = WITA.strftime('%d%m%y')
    jam = str(WITA.strftime('%H')).zfill(2)
    username = base_name + tgl + "C" + jam
    return username


def get_password(base_name:str) -> str : 
    """Membuat password untuk API"""
    tgl = NOW.strftime('%d-%m-%y')
    password = base_name + str(tgl)
    return hashlib.md5(password.encode()).hexdigest()


def normalize_api_data(response) -> list:
    """Khusus mengambil nilai 'data' dari API"""
    response = response['response']
    data = json.loads(response)
    data = data.get('data')
    return data


def get_or_create_kategori(data_kategori) -> Kategori:
    """Ambil atau tambah data kategori baru"""
    kategori, _ = Kategori.objects.get_or_create(nama_kategori=data_kategori)
    return kategori


def get_or_create_status(data_status) -> Status:
    """Ambil atau tambah data status baru"""
    status, _ = Status.objects.get_or_create(nama_status=data_status)
    return status

