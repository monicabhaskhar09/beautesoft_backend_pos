# Generated by Django 3.0.7 on 2023-07-17 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cl_app', '0013_tmpitemhelpersession'),
        ('cl_table', '0023_treatment'),
    ]

    operations = [
        migrations.CreateModel(
            name='TreatmentPackage',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('treatment_parentcode', models.CharField(blank=True, db_column='Treatment_ParentCode', max_length=20, null=True)),
                ('item_code', models.CharField(blank=True, db_column='Item_Code', max_length=20, null=True)),
                ('course', models.CharField(blank=True, db_column='Course', max_length=255, null=True)),
                ('treatment_no', models.CharField(blank=True, db_column='Treatment_No', max_length=10, null=True)),
                ('open_session', models.IntegerField(blank=True, db_column='open_session', null=True)),
                ('done_session', models.IntegerField(blank=True, db_column='done_session', null=True)),
                ('cancel_session', models.IntegerField(blank=True, db_column='cancel_session', null=True)),
                ('expiry_date', models.DateTimeField(blank=True, db_column='Expiry_Date', null=True)),
                ('unit_amount', models.FloatField(blank=True, db_column='Unit_Amount', null=True)),
                ('cust_name', models.CharField(blank=True, db_column='Cust_Name', max_length=100, null=True)),
                ('cust_code', models.CharField(blank=True, db_column='Cust_Code', max_length=50, null=True)),
                ('totalprice', models.FloatField(blank=True, db_column='Price', null=True)),
                ('type', models.CharField(blank=True, db_column='Type', max_length=50, null=True)),
                ('lastsession_unit_amount', models.FloatField(blank=True, db_column='lastsession_unit_amount', null=True)),
                ('treatment_date', models.DateTimeField(auto_now_add=True, db_column='Treatment_Date', null=True)),
                ('treatment_limit_times', models.FloatField(blank=True, db_column='Treatment_Limit_Times', null=True)),
                ('site_code', models.CharField(blank=True, db_column='Site_Code', max_length=50, null=True)),
                ('sa_transacno', models.CharField(blank=True, max_length=200, null=True)),
                ('sa_transacno_ref', models.CharField(blank=True, db_column='SA_TransacNo_Ref', max_length=200, null=True)),
                ('balance', models.FloatField(db_column='Balance', null=True)),
                ('outstanding', models.FloatField(blank=True, db_column='Outstanding', null=True)),
                ('Item_Codeid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_table.Stock')),
                ('Site_Codeid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_app.ItemSitelist')),
                ('customerid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_table.Customer')),
                ('treatment_accountid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_table.TreatmentAccount')),
            ],
            options={
                'db_table': 'Treatment_Package',
            },
        ),
    ]
