# Generated by Django 2.0.7 on 2018-07-13 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0002_delete_matakuliah'),
    ]

    operations = [
        migrations.CreateModel(
            name='MataPerkuliahan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount_sks', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'mataperkuliahan',
                'ordering': ['id'],
            },
        ),
    ]
