# Generated by Django 3.0.7 on 2023-07-17 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0058_alldropdownmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupplyContactInfoModel',
            fields=[
                ('ContactInfo_ID', models.AutoField(db_column='ContactInfo_ID', primary_key=True, serialize=False)),
                ('Supplier_Code', models.CharField(blank=True, db_column='Supplier_Code', default='', max_length=255, null=True)),
                ('ContactInfo_Name', models.CharField(blank=True, db_column='ContactInfo_Name', default='', max_length=255, null=True)),
                ('ContactInfo_PhoneNo', models.CharField(blank=True, db_column='ContactInfo_PhoneNo', default='', max_length=255, null=True)),
                ('ContactInfo_Email', models.CharField(blank=True, db_column='ContactInfo_Email', default='', max_length=255, null=True)),
                ('Active', models.CharField(blank=True, db_column='Active', default='active', max_length=255, null=True)),
            ],
            options={
                'db_table': 'Supply_ContactInfo',
            },
        ),
    ]