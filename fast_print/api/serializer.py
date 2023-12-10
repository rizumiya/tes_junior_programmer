from rest_framework import serializers

from kategori.models import Kategori
from status.models import Status
from produk.models import Produk


class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = '__all__'

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

class ProdukSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produk
        fields = '__all__'

    # def validate_nama_produk(self, value):
    #     if Produk.objects.filter(nama_produk=value).exists():
    #         raise serializers.ValidationError('The name of the product already exists', 'duplicate')
    #     return value
