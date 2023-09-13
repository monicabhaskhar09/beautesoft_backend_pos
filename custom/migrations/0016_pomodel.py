# Generated by Django 3.0.7 on 2023-07-17 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0112_invoicetemplate'),
        ('custom', '0015_datechangelog'),
    ]

    operations = [
        migrations.CreateModel(
            name='POModel',
            fields=[
                ('id', models.AutoField(db_column='PO_ID', primary_key=True, serialize=False)),
                ('po_number', models.CharField(blank=True, db_column='PO_Number', default='', max_length=255, null=True)),
                ('title', models.CharField(blank=True, db_column='PO_Project', default='', max_length=255, null=True)),
                ('company', models.CharField(blank=True, db_column='PO_Company', default='', max_length=255, null=True)),
                ('contact_person', models.CharField(blank=True, db_column='PO_ContactPerson', default='', max_length=255, null=True)),
                ('status', models.CharField(blank=True, db_column='PO_Status', default='', max_length=255, null=True)),
                ('in_charge', models.CharField(blank=True, db_column='PO_InCharge', default='', max_length=255, null=True)),
                ('remarks', models.CharField(blank=True, db_column='PO_Remarks', default='', max_length=255, null=True)),
                ('active', models.CharField(blank=True, db_column='Active', default='active', max_length=255, null=True)),
                ('created_at', models.DateTimeField(db_column='PO_Date', null=True)),
                ('cust_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_table.Customer')),
            ],
            options={
                'db_table': 'PurchaseOrder_List',
            },
        ),
    ]
