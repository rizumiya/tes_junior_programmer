# Generated by Django 5.0 on 2023-12-10 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id_status', models.BigAutoField(primary_key=True, serialize=False)),
                ('nama_status', models.CharField(max_length=120)),
            ],
        ),
    ]
