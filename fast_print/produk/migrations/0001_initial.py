# Generated by Django 5.0 on 2023-12-10 13:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('kategori', '0001_initial'),
        ('status', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produk',
            fields=[
                ('id_produk', models.BigAutoField(primary_key=True, serialize=False)),
                ('nama_produk', models.CharField(max_length=120)),
                ('harga', models.IntegerField()),
                ('kategori_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produk', to='kategori.kategori')),
                ('status_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='produk', to='status.status')),
            ],
        ),
    ]
