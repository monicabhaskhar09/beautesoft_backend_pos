# Generated by Django 3.0.7 on 2023-09-19 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0128_auto_20230919_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatmentduration',
            name='duration',
            field=models.TimeField(),
        ),
    ]