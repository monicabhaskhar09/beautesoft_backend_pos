# Generated by Django 3.0.7 on 2023-07-17 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0039_podetailmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuotationItemModel',
            fields=[
                ('id', models.AutoField(db_column='Quotation_Item_ID', primary_key=True, serialize=False)),
                ('quotation_quantity', models.CharField(blank=True, db_column='Quotation_Item_Quantity', default='', max_length=255, null=True)),
                ('quotation_unitprice', models.CharField(blank=True, db_column='Quotation_Item_UnitPrice', default='', max_length=255, null=True)),
                ('quotation_itemremarks', models.CharField(blank=True, db_column='Quotation_Item_Remarks', default='', max_length=255, null=True)),
                ('quotation_itemcode', models.CharField(blank=True, db_column='Quotation_Item_Code', default='', max_length=255, null=True)),
                ('quotation_itemdesc', models.CharField(blank=True, db_column='Quotation_Item_Desc', default='', max_length=255, null=True)),
                ('active', models.CharField(blank=True, db_column='Active', default='active', max_length=255, null=True)),
                ('discount_percent', models.FloatField(default=0.0, null=True)),
                ('discount_amt', models.FloatField(default=0.0, null=True)),
                ('fk_quotation', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='custom.QuotationModel')),
            ],
            options={
                'db_table': 'Quotation_Item',
            },
        ),
    ]