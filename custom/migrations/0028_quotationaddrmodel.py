# Generated by Django 3.0.7 on 2023-07-17 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0027_deliveryordermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuotationAddrModel',
            fields=[
                ('id', models.AutoField(db_column='Quotation_Addr_ID', primary_key=True, serialize=False)),
                ('billto', models.CharField(blank=True, db_column='Quotation_Bill_To', default='', max_length=255, null=True)),
                ('bill_addr1', models.CharField(blank=True, db_column='Quotation_Bill_Addr1', default='', max_length=255, null=True)),
                ('bill_addr2', models.CharField(blank=True, db_column='Quotation_Bill_Addr2', default='', max_length=255, null=True)),
                ('bill_addr3', models.CharField(blank=True, db_column='Quotation_Bill_Addr3', default='', max_length=255, null=True)),
                ('bill_postalcode', models.CharField(blank=True, db_column='Quotation_Bill_PostalCode', default='', max_length=255, null=True)),
                ('bill_city', models.CharField(blank=True, db_column='Quotation_Bill_City', default='', max_length=255, null=True)),
                ('bill_state', models.CharField(blank=True, db_column='Quotation_Bill_State', default='', max_length=255, null=True)),
                ('bill_country', models.CharField(blank=True, db_column='Quotation_Bill_Country', default='', max_length=255, null=True)),
                ('shipto', models.CharField(blank=True, db_column='Quotation_Ship_To', default='', max_length=255, null=True)),
                ('ship_addr1', models.CharField(blank=True, db_column='Quotation_Ship_Addr1', default='', max_length=255, null=True)),
                ('ship_addr2', models.CharField(blank=True, db_column='Quotation_Ship_Addr2', default='', max_length=255, null=True)),
                ('ship_addr3', models.CharField(blank=True, db_column='Quotation_Ship_Addr3', default='', max_length=255, null=True)),
                ('ship_postalcode', models.CharField(blank=True, db_column='Quotation_Ship_PostalCode', default='', max_length=255, null=True)),
                ('ship_city', models.CharField(blank=True, db_column='Quotation_Ship_City', default='', max_length=255, null=True)),
                ('ship_state', models.CharField(blank=True, db_column='Quotation_Ship_State', default='', max_length=255, null=True)),
                ('ship_country', models.CharField(blank=True, db_column='Quotation_Ship_Country', default='', max_length=255, null=True)),
                ('active', models.CharField(blank=True, db_column='Active', default='active', max_length=255, null=True)),
                ('fk_quotation', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='custom.QuotationModel')),
            ],
            options={
                'db_table': 'Quotation_Address',
            },
        ),
    ]
