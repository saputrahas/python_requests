# Generated by Django 2.0.7 on 2018-07-13 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mahasiswa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'mahasiswa',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Matakuliah',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount_sks', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'matakuliah',
                'ordering': ['id'],
            },
        ),
    ]
