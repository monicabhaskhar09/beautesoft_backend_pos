# Generated by Django 3.0.7 on 2023-07-17 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0092_customerpoint'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerPointDtl',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('transacno', models.CharField(db_column='TransacNo', max_length=20)),
                ('type', models.CharField(blank=True, db_column='Type', max_length=50, null=True)),
                ('cust_code', models.CharField(db_column='Cust_Code', max_length=20)),
                ('cust_name', models.CharField(blank=True, db_column='Cust_Name', max_length=100, null=True)),
                ('parent_code', models.CharField(blank=True, db_column='Parent_Code', max_length=20, null=True)),
                ('parent_desc', models.CharField(blank=True, db_column='Parent_Desc', max_length=50, null=True)),
                ('parent_display', models.CharField(blank=True, db_column='Parent_Display', max_length=100, null=True)),
                ('itm_code', models.CharField(blank=True, db_column='itm_Code', max_length=20, null=True)),
                ('itm_desc', models.CharField(blank=True, db_column='itm_Desc', max_length=50, null=True)),
                ('point', models.FloatField(db_column='Point')),
                ('now_point', models.FloatField(db_column='Now_Point')),
                ('remark', models.CharField(blank=True, db_column='Remark', max_length=100, null=True)),
                ('remark_code', models.CharField(blank=True, db_column='Remark_Code', max_length=20, null=True)),
                ('remark_desc', models.CharField(blank=True, db_column='Remark_Desc', max_length=50, null=True)),
                ('isvoid', models.BooleanField(db_column='Isvoid')),
                ('void_referenceno', models.CharField(blank=True, db_column='void_ReferenceNo', max_length=20, null=True)),
                ('isopen', models.BooleanField(blank=True, db_column='IsOpen', null=True)),
                ('qty', models.IntegerField(blank=True, db_column='Qty', null=True)),
                ('total_point', models.FloatField(blank=True, db_column='Total_Point', null=True)),
                ('seq', models.IntegerField(blank=True, db_column='Seq', null=True)),
                ('sa_status', models.CharField(blank=True, db_column='Sa_status', max_length=10, null=True)),
                ('bal_acc2', models.FloatField(blank=True, db_column='Bal_Acc2', null=True)),
                ('point_acc1', models.FloatField(blank=True, db_column='Point_Acc1', null=True)),
                ('point_acc2', models.FloatField(blank=True, db_column='Point_Acc2', null=True)),
                ('locid', models.CharField(db_column='LocID', max_length=50)),
                ('mgm_level', models.IntegerField(db_column='mgm_level', null=True)),
                ('reward_time', models.IntegerField(blank=True, db_column='reward_time', null=True)),
            ],
            options={
                'db_table': 'Customer_Point_Dtl',
                'unique_together': {('transacno', 'cust_code', 'point', 'now_point', 'locid')},
            },
        ),
    ]
