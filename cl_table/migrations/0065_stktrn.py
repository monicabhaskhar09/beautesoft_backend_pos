# Generated by Django 3.0.7 on 2023-07-17 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0064_itembatchsno'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stktrn',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('trn_post', models.DateTimeField(db_column='TRN_POST', null=True)),
                ('trn_no', models.FloatField(blank=True, db_column='TRN_NO', null=True)),
                ('trn_date', models.DateTimeField(db_column='TRN_DATE', null=True)),
                ('post_time', models.CharField(blank=True, db_column='POST_TIME', max_length=6, null=True)),
                ('aperiod', models.FloatField(blank=True, db_column='APERIOD', null=True)),
                ('itemcode', models.CharField(blank=True, db_column='ITEMCODE', max_length=15, null=True)),
                ('store_no', models.CharField(blank=True, db_column='STORE_NO', max_length=20, null=True)),
                ('tstore_no', models.CharField(blank=True, db_column='TSTORE_NO', max_length=20, null=True)),
                ('fstore_no', models.CharField(blank=True, db_column='FSTORE_NO', max_length=20, null=True)),
                ('trn_docno', models.CharField(blank=True, db_column='TRN_DOCNO', max_length=20, null=True)),
                ('trn_type', models.CharField(blank=True, db_column='TRN_TYPE', max_length=10, null=True)),
                ('trn_db_qty', models.FloatField(blank=True, db_column='TRN_DB_QTY', null=True)),
                ('trn_cr_qty', models.FloatField(blank=True, db_column='TRN_CR_QTY', null=True)),
                ('trn_qty', models.FloatField(blank=True, db_column='TRN_QTY', null=True)),
                ('trn_balqty', models.FloatField(blank=True, db_column='TRN_BALQTY', null=True)),
                ('trn_balcst', models.FloatField(blank=True, db_column='TRN_BALCST', null=True)),
                ('trn_amt', models.FloatField(blank=True, db_column='TRN_AMT', null=True)),
                ('trn_cost', models.FloatField(blank=True, db_column='TRN_COST', null=True)),
                ('trn_ref', models.CharField(blank=True, db_column='TRN_REF', max_length=8, null=True)),
                ('hq_update', models.BooleanField(db_column='HQ_UPDATE', null=True)),
                ('line_no', models.FloatField(blank=True, db_column='LINE_NO', null=True)),
                ('item_uom', models.CharField(blank=True, db_column='Item_UOM', max_length=20, null=True)),
                ('item_batch', models.CharField(blank=True, db_column='Item_Batch', max_length=20, null=True)),
                ('mov_type', models.CharField(blank=True, db_column='Mov_type', max_length=10, null=True)),
                ('item_batch_cost', models.FloatField(blank=True, db_column='Item_Batch_Cost', null=True)),
                ('stock_in', models.BooleanField(blank=True, db_column='Stock_In', null=True)),
                ('trans_package_line_no', models.FloatField(blank=True, db_column='TRANS_PACKAGE_LINE_NO', null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'Stktrn',
            },
        ),
    ]
