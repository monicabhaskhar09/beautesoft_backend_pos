# Generated by Django 3.0.7 on 2023-07-17 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0008_auto_20230717_1317'),
        ('cl_table', '0053_itemhelper'),
    ]

    operations = [
        migrations.AddField(
            model_name='tmpitemhelper',
            name='pospackage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='custom.PosPackagedeposit'),
        ),
    ]