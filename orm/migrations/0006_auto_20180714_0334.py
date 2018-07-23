# Generated by Django 2.0.7 on 2018-07-14 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0005_mahasiswa_year_in_school'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mahasiswa',
            name='year_in_school',
        ),
        migrations.AddField(
            model_name='mahasiswa',
            name='Gender',
            field=models.CharField(choices=[('PR', 'Pria'), ('PR', 'Wanita')], default='PR', max_length=2),
        ),
    ]
