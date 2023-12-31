# Generated by Django 3.0.7 on 2023-07-17 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cl_app', '0013_tmpitemhelpersession'),
        ('cl_table', '0039_prepaidaccount'),
    ]

    operations = [
        migrations.CreateModel(
            name='DepositAccount',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('cust_code', models.CharField(db_column='Cust_Code', max_length=20, null=True)),
                ('sa_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('type', models.CharField(blank=True, choices=[('Deposit', 'Deposit'), ('Top Up', 'Top Up'), ('CANCEL', 'CANCEL')], db_column='Type', max_length=10, null=True)),
                ('amount', models.FloatField(blank=True, db_column='Amount', null=True)),
                ('balance', models.FloatField(blank=True, db_column='Balance', null=True)),
                ('user_name', models.CharField(blank=True, db_column='User_Name', max_length=50, null=True)),
                ('sa_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('qty', models.IntegerField(blank=True, db_column='Qty', null=True)),
                ('outstanding', models.FloatField(blank=True, db_column='Outstanding', null=True)),
                ('deposit', models.FloatField(blank=True, db_column='Deposit', null=True)),
                ('cas_logno', models.CharField(blank=True, max_length=20, null=True)),
                ('mac_code', models.CharField(blank=True, max_length=20, null=True)),
                ('cas_name', models.CharField(blank=True, max_length=60, null=True)),
                ('sa_staffno', models.CharField(blank=True, max_length=50, null=True)),
                ('sa_staffname', models.CharField(blank=True, max_length=60, null=True)),
                ('deposit_type', models.CharField(blank=True, db_column='Deposit_Type', max_length=50, null=True)),
                ('sa_transacno', models.CharField(db_column='sa_Transacno', max_length=50, null=True)),
                ('description', models.CharField(blank=True, db_column='Description', max_length=100, null=True)),
                ('ref_code', models.CharField(db_column='Ref_Code', max_length=100, null=True)),
                ('sa_status', models.CharField(blank=True, db_column='SA_STATUS', max_length=50, null=True)),
                ('item_barcode', models.CharField(db_column='Item_Barcode', max_length=50, null=True)),
                ('item_description', models.CharField(blank=True, db_column='Item_Description', max_length=100, null=True)),
                ('treat_code', models.CharField(blank=True, db_column='Treat_Code', max_length=50, null=True)),
                ('void_link', models.CharField(blank=True, db_column='Void_Link', max_length=50, null=True)),
                ('lpackage', models.BooleanField(db_column='lPackage', null=True)),
                ('package_code', models.CharField(blank=True, db_column='Package_Code', max_length=50, null=True)),
                ('dt_lineno', models.IntegerField(db_column='dt_LineNo', null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('site_code', models.CharField(db_column='Site_Code', max_length=50, null=True)),
                ('item_code', models.CharField(blank=True, db_column='Item_Code', max_length=20, null=True)),
                ('ref_transacno', models.CharField(blank=True, db_column='Ref_Transacno', max_length=20, null=True)),
                ('ref_productcode', models.CharField(blank=True, db_column='Ref_ProductCode', max_length=20, null=True)),
                ('Cust_Codeid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_table.Customer')),
                ('Item_Codeid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_table.Stock')),
                ('Site_Codeid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_app.ItemSitelist')),
            ],
            options={
                'db_table': 'Deposit_Account',
            },
        ),
    ]
