# Generated by Django 3.0.7 on 2023-07-17 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0057_systemlogmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllDropdownModel',
            fields=[
                ('AllDropdown_ID', models.AutoField(db_column='AllDropdown_ID', primary_key=True, serialize=False)),
                ('AllDropdown_Item', models.CharField(blank=True, db_column='AllDropdown_Item', default='', max_length=255, null=True)),
                ('AllDropdown_Desc', models.CharField(blank=True, db_column='AllDropdown_Desc', default='', max_length=255, null=True)),
                ('Active', models.CharField(blank=True, db_column='Active', default='active', max_length=255, null=True)),
            ],
            options={
                'db_table': 'AllDropdown_List',
            },
        ),
    ]
