# Generated by Django 2.0.7 on 2018-07-14 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0009_mahasiswa_gender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mahasiswa',
            old_name='gender',
            new_name='jenis_kelamin',
        ),
    ]
