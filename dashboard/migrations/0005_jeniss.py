# Generated by Django 4.1.2 on 2022-11-25 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_minuman'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jeniss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('ket', models.TextField()),
            ],
        ),
    ]