# Generated by Django 3.0.7 on 2023-07-17 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0034_quotationpayment'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManualInvoiceDetailModel',
            fields=[
                ('id', models.AutoField(db_column=' ManualInvoice_Detail_ID', primary_key=True, serialize=False)),
                ('q_shipcost', models.CharField(blank=True, db_column=' ManualInvoice_ShipCost', default='', max_length=255, null=True)),
                ('q_discount', models.CharField(blank=True, db_column=' ManualInvoice_Discount', default='', max_length=255, null=True)),
                ('q_discpercent', models.FloatField(default=0.0, null=True)),
                ('q_taxes', models.CharField(blank=True, db_column='ManualInvoice_Taxes', default='', max_length=255, null=True)),
                ('q_total', models.CharField(blank=True, db_column=' ManualInvoice_Total', default='', max_length=255, null=True)),
                ('active', models.CharField(blank=True, db_column='Active', default='active', max_length=255, null=True)),
                ('fk_manualinvoice', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='custom.ManualInvoiceModel')),
            ],
            options={
                'db_table': 'ManualInvoice_Detail',
            },
        ),
    ]
