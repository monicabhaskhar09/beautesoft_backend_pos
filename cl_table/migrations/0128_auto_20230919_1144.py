# Generated by Django 3.0.7 on 2023-09-19 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0127_auto_20230916_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatmentduration',
            name='duration',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
