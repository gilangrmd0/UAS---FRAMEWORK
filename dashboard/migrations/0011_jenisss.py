# Generated by Django 4.1.2 on 2023-02-02 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_rename_jeniss_id_promo_jenisss_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jenisss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('ket', models.TextField()),
            ],
        ),
    ]
