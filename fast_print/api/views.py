import requests

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .utils import get_password, get_username, normalize_api_data, get_or_create_kategori, get_or_create_status
from .serializer import ProdukSerializer
from produk.models import Produk


def get_data_api(request):
    """Ambil data api"""

    url = 'https://recruitment.fastprint.co.id/tes/api_tes_programmer'
    usern = get_username("tesprogrammer")
    passw = get_password("bisacoding-")

    payload = {
        'username': usern,
        'password': passw
    }

    response = requests.post(url, data=payload)
    # print("header: ", response.headers)
    # print("cookies: ", response.cookies)
    
    return response.text


@api_view(['POST'])
def save_to_database(request):
    """Menyimpan data hasil normalisasi data API ke database"""
    datas = normalize_api_data(request.data)
    responses = []

    if datas and len(datas) > 0:
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
                print(serializer.errors)
                continue
                
    if any(isinstance(response, dict) for response in responses):
        # jika seluruh isinya bertipe dict -> berhasil
        return cek_data(request)


def cek_data(request):
    """Cek data dalam database"""
    if Produk.objects.exists():
        # menuju ke halaman utama
        return HttpResponseRedirect('home/')
    else:
        # menuju ke halaman api
        return HttpResponseRedirect('api/')

class MainMenu(View):
    def get(self, request):
        """Menampilkan keseluruhan data"""
        semua_data = request.GET.get('semua_data')

        if semua_data == None:
            semua_data = False

        if semua_data:
            produk = Produk.objects.all()
            return render(request, 'tampil_data.html', {'data_produk': True, 'semua_data': semua_data, 'data': produk})
        
        produk = Produk.objects.filter(status_id__nama_status__iexact='bisa dijual')
        return render(request, 'tampil_data.html', {'data_produk': True, 'semua_data': semua_data, 'data': produk})


def api_page(request):
    """Mengambil data API dan menampilkannya di halaman API"""
    response = get_data_api(request)
    return render(request, 'api_page.html', {'data_produk': False, 'data': None, 'response_text': response})

