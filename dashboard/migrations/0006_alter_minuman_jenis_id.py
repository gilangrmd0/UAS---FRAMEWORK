# Generated by Django 4.1.2 on 2022-11-25 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_jeniss'),
    ]

    operations = [
        migrations.AlterField(
            model_name='minuman',
            name='jenis_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.jeniss'),
        ),
    ]