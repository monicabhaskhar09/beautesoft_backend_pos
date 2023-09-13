# Generated by Django 3.0.7 on 2023-07-17 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0034_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditNote',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('sa_date', models.DateTimeField(auto_now_add=True, db_column='sa_Date', null=True)),
                ('treatment_code', models.CharField(db_column='Treatment_Code', max_length=20)),
                ('treatment_name', models.CharField(blank=True, db_column='Treatment_Name', max_length=200, null=True)),
                ('amount', models.FloatField(blank=True, db_column='Amount', null=True)),
                ('treatment_parentcode', models.CharField(blank=True, db_column='Treatment_ParentCode', max_length=20, null=True)),
                ('type', models.CharField(blank=True, db_column='Type', max_length=20, null=True)),
                ('cust_code', models.CharField(blank=True, db_column='Cust_Code', max_length=50, null=True)),
                ('cust_name', models.CharField(blank=True, db_column='Cust_Name', max_length=100, null=True)),
                ('sa_transacno', models.CharField(blank=True, max_length=20, null=True)),
                ('status', models.CharField(blank=True, choices=[('OPEN', 'OPEN'), ('CLOSE', 'CLOSE')], db_column='Status', max_length=10, null=True)),
                ('credit_code', models.CharField(db_column='Credit_Code', max_length=20)),
                ('balance', models.FloatField(blank=True, db_column='Balance', null=True)),
                ('deposit_type', models.CharField(blank=True, db_column='Deposit_Type', max_length=50, null=True)),
                ('site_code', models.CharField(db_column='Site_Code', max_length=50)),
                ('treat_code', models.CharField(blank=True, db_column='Treat_Code', max_length=50, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'Credit_Note',
            },
        ),
    ]
