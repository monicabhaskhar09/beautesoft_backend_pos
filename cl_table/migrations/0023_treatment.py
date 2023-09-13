# Generated by Django 3.0.7 on 2023-07-17 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cl_app', '0013_tmpitemhelpersession'),
        ('custom', '0005_voucherrecord'),
        ('cl_table', '0022_tmpitemhelper'),
    ]

    operations = [
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('sys_code', models.AutoField(db_column='Sys_Code', primary_key=True, serialize=False)),
                ('treatment_code', models.CharField(db_column='Treatment_Code', max_length=200, null=True)),
                ('course', models.CharField(blank=True, db_column='Course', max_length=255, null=True)),
                ('times', models.CharField(blank=True, db_column='Times', max_length=10, null=True)),
                ('treatment_no', models.CharField(blank=True, db_column='Treatment_No', max_length=10, null=True)),
                ('price', models.FloatField(blank=True, db_column='Price', null=True)),
                ('treatment_date', models.DateTimeField(auto_now_add=True, db_column='Treatment_Date', null=True)),
                ('cust_name', models.CharField(blank=True, db_column='Cust_Name', max_length=100, null=True)),
                ('cust_code', models.CharField(blank=True, db_column='Cust_Code', max_length=50, null=True)),
                ('status', models.CharField(blank=True, choices=[('Open', 'Open'), ('Done', 'Done'), ('Cancel', 'Cancel')], db_column='Status', default='open', max_length=50, null=True)),
                ('unit_amount', models.FloatField(blank=True, db_column='Unit_Amount', null=True)),
                ('item_code', models.CharField(blank=True, db_column='Item_Code', max_length=20, null=True)),
                ('treatment_parentcode', models.CharField(blank=True, db_column='Treatment_ParentCode', max_length=20, null=True)),
                ('sa_transacno', models.CharField(blank=True, max_length=20, null=True)),
                ('sa_status', models.CharField(blank=True, choices=[('SA', 'SA'), ('VOID', 'VOID'), ('SU', 'SU')], max_length=5, null=True)),
                ('record_status', models.CharField(blank=True, choices=[('PENDING', 'PENDING')], db_column='Record_Status', max_length=10, null=True)),
                ('remarks', models.CharField(blank=True, db_column='Remarks', max_length=255, null=True)),
                ('duration', models.IntegerField(blank=True, db_column='Duration', null=True)),
                ('transaction_time', models.DateTimeField(blank=True, db_column='Transaction_Time', null=True)),
                ('dt_lineno', models.IntegerField(blank=True, db_column='dt_LineNo', null=True)),
                ('expiry', models.DateTimeField(blank=True, db_column='Expiry', null=True)),
                ('package_code', models.CharField(blank=True, db_column='Package_Code', max_length=50, null=True)),
                ('site_code', models.CharField(blank=True, db_column='Site_Code', max_length=50, null=True)),
                ('type', models.CharField(blank=True, db_column='Type', max_length=50, null=True)),
                ('treatment_limit_times', models.FloatField(blank=True, db_column='Treatment_Limit_Times', null=True)),
                ('treatment_count_done', models.FloatField(blank=True, db_column='Treatment_Count_Done', null=True)),
                ('service_itembarcode', models.CharField(blank=True, db_column='Service_ItemBarcode', max_length=20, null=True)),
                ('isfoc', models.BooleanField(blank=True, db_column='isFOC', null=True)),
                ('trmt_room_code', models.CharField(blank=True, db_column='Trmt_Room_Code', max_length=50, null=True)),
                ('trmt_is_auto_proportion', models.BooleanField(db_column='Trmt_Is_Auto_Proportion', null=True)),
                ('flexipoints', models.FloatField(blank=True, db_column='flexipoints', null=True)),
                ('redeempoints', models.FloatField(blank=True, db_column='redeempoints', null=True)),
                ('Cust_Codeid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_table.Customer')),
                ('Item_Codeid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_table.Stock')),
                ('Site_Codeid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_app.ItemSitelist')),
                ('Trmt_Room_Codeid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='custom.Room')),
                ('helper_ids', models.ManyToManyField(blank=True, related_name='tmpitemhelper', to='cl_table.TmpItemHelper')),
                ('treatment_account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_table.TreatmentAccount')),
            ],
            options={
                'db_table': 'Treatment',
            },
        ),
    ]
