from django.http import HttpResponseRedirect
from django.shortcuts import render

from produk.views import atur_tampil_data
from produk.models import Produk
from status.models import Status


def show_home(request):
    """Menampilkan halaman utama"""
    content = {
        'status': Status.objects.all()
    }

    tampil, data = atur_tampil_data(request)
    content.update({'tampil_rad': tampil, 'data': data})

    return render(request, 'produk_detail.html', content)


def show_admin_pg(request):
    """Menampilkan halaman admin playground"""
    return render(request, 'produk_new.html', {})


def show_default(request):
    """Menampilkan halaman API jika data produk kosong"""
    if Produk.objects.exists():
        return HttpResponseRedirect('home/')
    return HttpResponseRedirect('api/')

