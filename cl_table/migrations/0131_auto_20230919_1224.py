# Generated by Django 3.0.7 on 2023-09-19 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0130_auto_20230919_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tmpitemhelper',
            name='add_duration',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='tmpitemhelper',
            name='appt_fr_time',
            field=models.TimeField(db_column='Appt_Fr_time', null=True),
        ),
        migrations.AlterField(
            model_name='tmpitemhelper',
            name='appt_to_time',
            field=models.TimeField(db_column='Appt_To_time', null=True),
        ),
    ]