import json
import hashlib
import datetime

from rest_framework.serializers import ModelSerializer

from kategori.models import Kategori
from status.models import Status


NOW = datetime.datetime.now()
WITA = NOW + datetime.timedelta(hours=1)

def get_username(basename:str) -> str :
    """Membuat username berdasarkan format yang ditentukan"""
    tgl = WITA.strftime('%d%m%y')
    jam = WITA.strftime('%H').zfill(2)
    username = basename + tgl + "C" + jam
    return username


def get_password(basename:str) -> str :
    """Membuat password berdasarkan format yang ditentukan"""
    tgl = WITA.strftime('%d-%m-%y')
    enc_pass = basename + tgl
    password = hashlib.md5(enc_pass.encode()).hexdigest()
    return password


def normalize_api_data(json_data):
    """Hanya mengambil nilai 'data'"""
    data = json.loads(json_data)
    data = data['data']
    return data


def get_or_create_kategori(nama_kategori) -> Kategori:
    kategori, _ = Kategori.objects.get_or_create(nama_kategori=nama_kategori)
    return kategori


def get_or_create_status(nama_status) -> Status:
    status, _ = Status.objects.get_or_create(nama_status=nama_status)
    return status


def cek_validitas(serializer: ModelSerializer) -> ModelSerializer:
    """Fungsi khusus untuk cek validasi serializer"""
    if serializer.is_valid():
        serializer.save()
        message = 'Data berhasil ditambahkan'
        status = True
    else:
        message = serializer.errors
        status = False

    content = {
        'message': message,
        'status': status
    }

    return content
