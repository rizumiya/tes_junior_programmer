from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.db.models.deletion import ProtectedError

from status.models import Status
from api.serializer import StatusSerializer
from api.utils import cek_validitas


def tambah_data_status(request):
    """Fungsi untuk menambah data status"""
    data = {}
    
    if request.method == 'POST':
        data['nama_status'] = request.POST['nama_status']

        serializer = StatusSerializer(data=data)

        return cek_validitas(serializer)
    return None


def ubah_data_status(request):
    """Fungsi untuk mengubah data status"""
    data = {}

    if request.method == 'POST':
        status = get_object_or_404(Status, id_status=request.POST['id_status'])
        data['nama_status'] = request.POST['nama_status']
        
        serializer = StatusSerializer(instance=status, data=data)
        
        return cek_validitas(serializer)
    return None


def tampilan_status(request):
    """Menampilkan halaman status"""
    content = {
        'data': Status.objects.all().order_by('-id_status'),
    }

    content.update({'message': None, 'errors': None, 'selected_data': None})
    
    # Menambahkan data
    response = tambah_data_status(request)
    if response:
        if response['status']:
            content.update({'message': response['message'], 'errors': None})
        else:
            content.update({'errors': response['message'], 'message': None})

    return render(request, 'status.html', content)


def tampilan_update_status(request, id_status):
    """Menampilkan halaman update data status"""
    content = {
        'data': Status.objects.all().order_by('-id_status'),
    }

    ubah_status = Status.objects.get(id_status=id_status)
    content.update({'selected_data': ubah_status})

    response = ubah_data_status(request)
    if response:
        if response['status']:
            return HttpResponseRedirect(reverse('status'))
        else:
            content.update({'errors': response['message'], 'message': None})
    
    return render(request, 'status.html', content)


def hapus_status(request, id_status):
    """Fungsi menghapus data status"""
    status = Status.objects.get(id_status=id_status)
    content = {
        'data': Status.objects.all().order_by('-id_status'),
    }

    try:
        status.delete()
        return JsonResponse({'message': 'Data status berhasil dihapus'})
    except ProtectedError:
        return JsonResponse({'error': 'Tidak dapat menghapus status karena masih ada data yang terkait'})


    

