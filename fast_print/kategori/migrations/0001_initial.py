# Generated by Django 5.0 on 2023-12-10 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id_kategori', models.BigAutoField(primary_key=True, serialize=False)),
                ('nama_kategori', models.CharField(max_length=120)),
            ],
        ),
    ]
