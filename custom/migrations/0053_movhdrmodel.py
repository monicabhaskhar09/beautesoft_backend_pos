# Generated by Django 3.0.7 on 2023-07-17 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0052_stktrnmodel_stockmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovHdrModel',
            fields=[
                ('PO_ID', models.AutoField(db_column='PO_ID', primary_key=True, serialize=False)),
                ('DOC_NO', models.CharField(blank=True, db_column='DOC_NO', default='', max_length=255, null=True)),
                ('MOV_CODE', models.CharField(blank=True, db_column='MOV_CODE', default='', max_length=255, null=True)),
                ('MOV_TYPE', models.CharField(blank=True, db_column='MOV_TYPE', default='', max_length=255, null=True)),
                ('STORE_NO', models.CharField(blank=True, db_column='STORE_NO', default='', max_length=255, null=True)),
                ('FSTORE_NO', models.CharField(blank=True, db_column='FSTORE_NO', default='', max_length=255, null=True)),
                ('TSTORE_NO', models.CharField(blank=True, db_column='TSTORE_NO', default='', max_length=255, null=True)),
                ('SUPPLY_NO', models.CharField(blank=True, db_column='SUPPLY_NO', default='', max_length=255, null=True)),
                ('DOC_REF1', models.CharField(blank=True, db_column='DOC_REF1', default='', max_length=255, null=True)),
                ('DOC_REF2', models.CharField(blank=True, db_column='DOC_REF2', default='', max_length=255, null=True)),
                ('ACC_CODE', models.CharField(blank=True, db_column='ACC_CODE', default='', max_length=255, null=True)),
                ('STAFF_NO', models.CharField(blank=True, db_column='STAFF_NO', default='', max_length=255, null=True)),
                ('DOC_LINES', models.FloatField(blank=True, db_column='DOC_LINES', null=True)),
                ('DOC_DATE', models.DateTimeField(auto_now_add=True, db_column='DOC_DATE', null=True)),
                ('POST_DATE', models.DateTimeField(auto_now_add=True, db_column='POST_DATE', null=True)),
                ('DOC_STATUS', models.FloatField(blank=True, db_column='DOC_STATUS', null=True)),
                ('DOC_TERM', models.CharField(blank=True, db_column='DOC_TERM', default='', max_length=255, null=True)),
                ('DOC_TIME', models.FloatField(blank=True, db_column='DOC_TIME', null=True)),
                ('DOC_QTY', models.FloatField(blank=True, db_column='DOC_QTY', null=True)),
                ('DOC_FOC', models.FloatField(blank=True, db_column='DOC_FOC', null=True)),
                ('DOC_DISC', models.FloatField(blank=True, db_column='DOC_DISC', null=True)),
                ('DOC_AMT', models.FloatField(blank=True, db_column='DOC_AMT', null=True)),
                ('DOC_TRNSPT', models.FloatField(blank=True, db_column='DOC_TRNSPT', null=True)),
                ('DOC_TAX', models.FloatField(blank=True, db_column='DOC_TAX', null=True)),
                ('DOC_ATTN', models.CharField(blank=True, db_column='DOC_ATTN', default='', max_length=255, null=True)),
                ('DOC_REMK1', models.CharField(blank=True, db_column='DOC_REMK1', default='', max_length=255, null=True)),
                ('DOC_REMK2', models.CharField(blank=True, db_column='DOC_REMK2', default='', max_length=255, null=True)),
                ('DOC_REMK3', models.CharField(blank=True, db_column='DOC_REMK3', default='', max_length=255, null=True)),
                ('DOC_SHIP', models.DateTimeField(db_column='DOC_SHIP', null=True)),
                ('BNAME', models.CharField(blank=True, db_column='BNAME', default='', max_length=255, null=True)),
                ('BADDR1', models.CharField(blank=True, db_column='BADDR1', default='', max_length=255, null=True)),
                ('BADDR2', models.CharField(blank=True, db_column='BADDR2', default='', max_length=255, null=True)),
                ('BADDR3', models.CharField(blank=True, db_column='BADDR3', default='', max_length=255, null=True)),
                ('BPOSTCODE', models.CharField(blank=True, db_column='BPOSTCODE', default='', max_length=255, null=True)),
                ('BSTATE', models.CharField(blank=True, db_column='BSTATE', default='', max_length=255, null=True)),
                ('BCITY', models.CharField(blank=True, db_column='BCITY', default='', max_length=255, null=True)),
                ('BCOUNTRY', models.CharField(blank=True, db_column='BCOUNTRY', default='', max_length=255, null=True)),
                ('DADDR1', models.CharField(blank=True, db_column='DADDR1', default='', max_length=255, null=True)),
                ('DADDR2', models.CharField(blank=True, db_column='DADDR2', default='', max_length=255, null=True)),
                ('DADDR3', models.CharField(blank=True, db_column='DADDR3', default='', max_length=255, null=True)),
                ('DPOSTCODE', models.CharField(blank=True, db_column='DPOSTCODE', default='', max_length=255, null=True)),
                ('DSTATE', models.CharField(blank=True, db_column='DSTATE', default='', max_length=255, null=True)),
                ('DCITY', models.CharField(blank=True, db_column='DCITY', default='', max_length=255, null=True)),
                ('DCOUNTRY', models.CharField(blank=True, db_column='DCOUNTRY', default='', max_length=255, null=True)),
                ('CANCEL_QTY', models.FloatField(blank=True, db_column='CANCEL_QTY', null=True)),
                ('REC_STATUS', models.FloatField(blank=True, db_column='REC_STATUS', null=True)),
                ('REC_EXPECT', models.DateTimeField(db_column='REC_EXPECT', null=True)),
                ('REC_TTL', models.FloatField(blank=True, db_column='REC_TTL', null=True)),
                ('CREATE_USER', models.CharField(blank=True, db_column='CREATE_USER', default='', max_length=255, null=True)),
                ('CREATE_DATE', models.DateTimeField(auto_now_add=True, db_column='CREATE_DATE', null=True)),
                ('PHY_NO', models.CharField(blank=True, db_column='PHY_NO', default='', max_length=255, null=True)),
                ('PO_NO', models.CharField(blank=True, db_column='PO_NO', default='', max_length=259, null=True)),
            ],
            options={
                'db_table': 'Stk_MovDoc_Hdr',
            },
        ),
    ]