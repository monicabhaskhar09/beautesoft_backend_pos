# Generated by Django 3.0.7 on 2023-09-14 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0120_taxtype2taxcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='cust_corporate',
            field=models.BooleanField(db_column='cust_corporate', default=False, null=True),
        ),
    ]
