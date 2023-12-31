# Generated by Django 3.0.7 on 2023-07-17 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0061_itemstocklist'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemLink',
            fields=[
                ('itm_id', models.AutoField(db_column='Itm_ID', primary_key=True, serialize=False)),
                ('link_code', models.CharField(db_column='LINK_CODE', max_length=20, null=True)),
                ('item_code', models.CharField(db_column='ITEM_CODE', max_length=20, null=True)),
                ('link_desc', models.CharField(blank=True, db_column='LINK_DESC', max_length=40, null=True)),
                ('link_factor', models.FloatField(blank=True, db_column='LINK_FACTOR', null=True)),
                ('link_type', models.CharField(blank=True, db_column='LINK_TYPE', max_length=1, null=True)),
                ('itm_isactive', models.BooleanField(blank=True, db_column='Itm_IsActive', default=True, null=True)),
                ('rpt_code_status', models.BooleanField(blank=True, db_column='Rpt_Code_Status', null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'Item_Link',
            },
        ),
    ]
