from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Produk
from kategori.models import Kategori
from status.models import Status

from api.serializer import ProdukSerializer
from api.utils import cek_validitas


def show_all(request):
    """Menampilkan seluruh data produk"""
    data = Produk.objects.all()
    return data


def show_partial(tampil):
    """Menampilkan sebagian data produk"""
    print(tampil)
    data = Produk.objects.filter(status_id__nama_status__iexact=tampil)
    return data


def tambah_data(request):
    """Method untuk menambahkan data produk baru"""
    data = {}
    
    if request.method == 'POST' and 'kategori_id' in request.POST:
        data['nama_produk'] = request.POST['nama_produk']
        data['harga'] = request.POST['harga']
        data['kategori_id'] = request.POST['kategori_id']
        data['status_id'] = request.POST['status_id']

        serializer = ProdukSerializer(data=data)

        return cek_validitas(serializer)
    return None


def ubah_data_produk(request):
    """Fungsi mengubah data produk"""
    data = {}

    if request.method == 'POST':
        produk = get_object_or_404(Produk, id_produk=request.POST['id_produk'])
        data['nama_produk'] = request.POST['nama_produk']
        data['harga'] = request.POST['harga']
        data['kategori_id'] = request.POST['kategori_id']
        data['status_id'] = request.POST['status_id']
        
        serializer = ProdukSerializer(instance=produk, data=data)
        
        return cek_validitas(serializer)
    return None


def atur_tampil_data(request):
    """Fungsi menampilkan seluruh atau sebagian data produk"""
    tampil = 'all'

    if request.method == 'POST' and 'show' in request.POST:
        tampil = request.POST['show']
            
    if tampil == 'all':
        data = show_all(request)
    else:
        data = show_partial(tampil)
    
    return tampil, data


def tampilan_produk(request):
    """Menampilkan data produk"""
    content = {
        'data': Produk.objects.all().order_by('-id_produk'),
        'kategori': Kategori.objects.all(),
        'status': Status.objects.all()
    }
    content.update({'message': None, 'errors': None, 'selected_data': None})

    # Mengatur banyak data yang ditampilkan
    tampil, data = atur_tampil_data(request)
    content.update({'tampil_rad': tampil, 'data': data.order_by('-id_produk')})
    
    # Menambahkan data
    response = tambah_data(request)
    if response:
        if response['status']:
            content.update({'message': response['message'], 'errors': None})
        else:
            content.update({'errors': response['message'], 'message': None})

    return render(request, 'produk.html', content)

        
def tampilan_update_produk(request, id_produk):
    """Menampilkan halaman update data produk"""
    content = {
        'data': Produk.objects.all().order_by('-id_produk'),
        'kategori': Kategori.objects.all(),
        'status': Status.objects.all()
    }
    tampil = None

    # Mengatur banyak data yang ditampilkan
    tampil, data = atur_tampil_data(request)
    content.update({'tampil_rad': tampil, 'data': data.order_by('-id_produk')})

    ubah_produk = Produk.objects.get(id_produk=id_produk)
    content.update({'selected_data': ubah_produk})

    response = ubah_data_produk(request)
    if response:
        if response['status']:
            return HttpResponseRedirect(reverse('produk'))
        else:
            content.update({'errors': response['message'], 'message': None})
    
    return render(request, 'produk.html', content)


def hapus_produk(request, id_produk):
    """Menghapus data produk"""
    produk = Produk.objects.get(id_produk=id_produk)
    produk.delete()

    return HttpResponseRedirect(reverse('produk'))

