from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect

from kategori.models import Kategori
from api.serializer import KategoriSerializer
from api.utils import cek_validitas


def tambah_data_kategori(request):
    """Fungsi untuk menambah data kategori"""
    data = {}
    
    if request.method == 'POST':
        data['nama_kategori'] = request.POST['nama_kategori']

        serializer = KategoriSerializer(data=data)

        return cek_validitas(serializer)
    return None


def ubah_data_kategori(request):
    """Fungsi untuk mengubah data kategori"""
    data = {}

    if request.method == 'POST':
        kategori = get_object_or_404(Kategori, id_kategori=request.POST['id_kategori'])
        data['nama_kategori'] = request.POST['nama_kategori']
        
        serializer = KategoriSerializer(instance=kategori, data=data)
        
        return cek_validitas(serializer)
    return None


def tampilan_kategori(request):
    """Menampilkan halaman kategori"""
    content = {
        'data': Kategori.objects.all().order_by('-id_kategori'),
    }

    content.update({'message': None, 'errors': None, 'selected_data': None})
    
    # Menambahkan data
    response = tambah_data_kategori(request)
    if response:
        if response['status']:
            content.update({'message': response['message'], 'errors': None})
        else:
            content.update({'errors': response['message'], 'message': None})

    return render(request, 'kategori.html', content)


def tampilan_update_kategori(request, id_kategori):
    """Menampilkan halaman update data kategori"""
    content = {
        'data': Kategori.objects.all().order_by('-id_kategori'),
    }

    ubah_kategori = Kategori.objects.get(id_kategori=id_kategori)
    content.update({'selected_data': ubah_kategori})

    response = ubah_data_kategori(request)
    if response:
        if response['status']:
            return HttpResponseRedirect(reverse('kategori'))
        else:
            content.update({'errors': response['message'], 'message': None})
    
    return render(request, 'kategori.html', content)


def hapus_kategori(request, id_kategori):
    """Fungsi menghapus data kategori"""
    kategori = Kategori.objects.get(id_kategori=id_kategori)
    kategori.delete()
    
    return HttpResponseRedirect(reverse('kategori'))

