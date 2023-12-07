from rest_framework import serializers

from produk.models import Produk


class ProdukSerializer(serializers.ModelSerializer):
    """Produk serializer"""

    class Meta:
        model = Produk
        fields = '__all__'

