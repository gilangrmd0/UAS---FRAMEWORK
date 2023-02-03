# Generated by Django 4.1.2 on 2022-11-25 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20221104_0907'),
    ]

    operations = [
        migrations.CreateModel(
            name='minuman',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kodemnm', models.CharField(max_length=8)),
                ('nama', models.CharField(max_length=50)),
                ('stok', models.IntegerField()),
                ('harga', models.BigIntegerField()),
                ('link_gbr', models.CharField(blank=True, max_length=150)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('jenis_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.jenis')),
            ],
        ),
    ]
