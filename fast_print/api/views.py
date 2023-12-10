import requests

from django.shortcuts import render
from rest_framework.decorators import api_view

from .serializer import ProdukSerializer
from .utils import get_password, get_username, normalize_api_data, get_or_create_kategori, get_or_create_status
from produk.models import Produk


def get_api_data(request):
    """Mengambil data dari API"""

    url = 'https://recruitment.fastprint.co.id/tes/api_tes_programmer'
    usern = get_username("tesprogrammer")
    passw = get_password("bisacoding-")

    # print(usern, passw)

    payload = {
        'username': usern,
        'password': passw,
    }

    response = requests.post(url, data=payload)
    # print(response.headers)
    # print(response.cookies)
    return response.text


def tampilan_get_api(request):
    """Menampilkan halaman untuk GET API data"""

    if request.method == 'POST':
        json_data = request.POST.get('ta_response', '')
        return simpan_data_api(request, json_data)
    
    data = True if Produk.objects.exists() else None
    
    response = get_api_data(request)
    return render(request, 'api_get.html', {'response': response, 'data': data})


def simpan_data_api(request, *args):
    """Menyimpan data API yang telah didapatkan"""
    datas = normalize_api_data(*args)
    responses = []

    if len(datas) > 0:
        for data in datas:
            kategori = get_or_create_kategori(data['kategori'])
            status = get_or_create_status(data['status'])

            data['kategori_id'] = kategori.id_kategori
            data['status_id'] = status.id_status

            serializer = ProdukSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                responses.append(serializer.data)
            else:
                responses.append(serializer.errors)
        
        if any(isinstance(response, dict) for response in responses):
            # jika isi dari response adalah bertipe dict, maka berhasil (tidak ada error)
            return render(request, 'api_get.html', {'response': None, 'data': True})
    
        
