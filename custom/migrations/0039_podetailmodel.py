# Generated by Django 3.0.7 on 2023-07-17 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0038_deliveryorderdetailmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='PODetailModel',
            fields=[
                ('id', models.AutoField(db_column='PO_Detail_ID', primary_key=True, serialize=False)),
                ('po_shipcost', models.CharField(blank=True, db_column='PO_ShipCost', default='', max_length=255, null=True)),
                ('po_discount', models.CharField(blank=True, db_column='PO_Discount', default='', max_length=255, null=True)),
                ('po_taxes', models.CharField(blank=True, db_column='PO_Taxes', default='', max_length=255, null=True)),
                ('po_total', models.CharField(blank=True, db_column='PO_Total', default='', max_length=255, null=True)),
                ('active', models.CharField(blank=True, db_column='Active', default='active', max_length=255, null=True)),
                ('fk_po', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='custom.POModel')),
            ],
            options={
                'db_table': 'PurchaseOrder_Detail',
            },
        ),
    ]
