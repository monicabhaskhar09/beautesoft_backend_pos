# Generated by Django 3.0.7 on 2023-07-17 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0112_invoicetemplate'),
        ('custom', '0024_quotationmodel_currency_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManualInvoiceModel',
            fields=[
                ('id', models.AutoField(db_column='ManualInvoice_ID', primary_key=True, serialize=False)),
                ('manualinv_number', models.CharField(blank=True, db_column='ManualInvoice_Number', default='', max_length=255, null=True)),
                ('title', models.CharField(blank=True, db_column='ManualInvoice_Project', default='', max_length=255, null=True)),
                ('company', models.CharField(blank=True, db_column='ManualInvoice_Company', default='', max_length=255, null=True)),
                ('contact_person', models.CharField(blank=True, db_column='ManualInvoice_ContactPerson', default='', max_length=255, null=True)),
                ('status', models.CharField(blank=True, db_column='ManualInvoice_Status', default='', max_length=255, null=True)),
                ('validity', models.CharField(blank=True, db_column='ManualInvoice_Validity', default='', max_length=255, null=True)),
                ('terms', models.CharField(blank=True, db_column='ManualInvoice_Terms', default='', max_length=255, null=True)),
                ('in_charge', models.CharField(blank=True, db_column='ManualInvoice_InCharge', default='', max_length=255, null=True)),
                ('remarks', models.CharField(blank=True, db_column='ManualInvoice_Remarks', default='', max_length=255, null=True)),
                ('footer', models.CharField(blank=True, db_column='ManualInvoice_Footer', default='', max_length=255, null=True)),
                ('active', models.CharField(blank=True, db_column='Active', default='active', max_length=255, null=True)),
                ('created_at', models.DateTimeField(db_column='ManualInvoice_Date', null=True)),
                ('sa_transacno_ref', models.CharField(max_length=255, null=True)),
                ('quotation_number', models.CharField(blank=True, db_column='Quotation_Number', default='', max_length=255, null=True)),
                ('isxeroposted', models.BooleanField(db_column='isxeroposted', default=False)),
                ('currency_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='custom.Currencytable')),
                ('cust_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_table.Customer')),
                ('fk_project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='custom.ProjectModel')),
            ],
            options={
                'db_table': 'ManualInvoice_List',
            },
        ),
    ]