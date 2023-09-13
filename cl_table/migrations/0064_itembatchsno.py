# Generated by Django 3.0.7 on 2023-07-17 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0063_itembatch'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemBatchSno',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('doc_no', models.CharField(blank=True, db_column='DOC_NO', max_length=30, null=True)),
                ('doc_outno', models.CharField(blank=True, db_column='DOC_OUTNO', max_length=30, null=True)),
                ('item_code', models.CharField(blank=True, db_column='ITEM_CODE', max_length=20, null=True)),
                ('site_code', models.CharField(blank=True, db_column='SITE_CODE', max_length=20, null=True)),
                ('batch_sno', models.CharField(blank=True, db_column='BATCH_SNO', max_length=300, null=True)),
                ('uom', models.CharField(blank=True, db_column='UOM', max_length=20, null=True)),
                ('availability', models.BooleanField(blank=True, db_column='Availability', null=True)),
                ('exp_date', models.DateTimeField(blank=True, db_column='EXP_DATE', null=True)),
                ('batch_cost', models.FloatField(blank=True, db_column='BATCH_COST', null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'ITEM_BATCHSNO',
                'unique_together': {('batch_sno',)},
            },
        ),
    ]
