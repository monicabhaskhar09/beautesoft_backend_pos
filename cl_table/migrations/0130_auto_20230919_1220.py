# Generated by Django 3.0.7 on 2023-09-19 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0129_auto_20230919_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tmpitemhelper',
            name='add_duration',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='tmpitemhelper',
            name='appt_fr_time',
            field=models.CharField(blank=True, db_column='Appt_Fr_time', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='tmpitemhelper',
            name='appt_to_time',
            field=models.CharField(blank=True, db_column='Appt_To_time', max_length=150, null=True),
        ),
    ]
