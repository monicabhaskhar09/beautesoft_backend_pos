# Generated by Django 3.0.7 on 2023-07-17 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0005_voucherrecord'),
        ('cl_table', '0021_treatmentaccount'),
    ]

    operations = [
        migrations.CreateModel(
            name='TmpItemHelper',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('item_code', models.CharField(blank=True, db_column='Item_Code', max_length=20, null=True)),
                ('item_name', models.CharField(blank=True, db_column='Item_Name', max_length=100, null=True)),
                ('line_no', models.IntegerField(blank=True, db_column='Line_No', null=True)),
                ('sa_transacno', models.CharField(blank=True, max_length=20, null=True)),
                ('amount', models.FloatField(blank=True, db_column='Amount', null=True)),
                ('helper_name', models.CharField(blank=True, db_column='Helper_Name', max_length=50, null=True)),
                ('helper_code', models.CharField(blank=True, db_column='Helper_Code', max_length=20, null=True)),
                ('sa_date', models.DateTimeField(blank=True, null=True)),
                ('site_code', models.CharField(blank=True, db_column='Site_Code', max_length=10, null=True)),
                ('wp1', models.FloatField(blank=True, db_column='WP1', null=True)),
                ('wp2', models.FloatField(blank=True, db_column='WP2', null=True)),
                ('wp3', models.FloatField(blank=True, db_column='WP3', null=True)),
                ('mac_uid_ref', models.CharField(blank=True, db_column='MAC_UID_Ref', max_length=50, null=True)),
                ('td_type_code', models.CharField(blank=True, db_column='TD_Type_CODE', max_length=50, null=True)),
                ('td_type_short_desc', models.CharField(blank=True, db_column='TD_Type_Short_Desc', max_length=50, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('appt_fr_time', models.TimeField(db_column='Appt_Fr_time', null=True)),
                ('appt_to_time', models.TimeField(db_column='Appt_To_time', null=True)),
                ('add_duration', models.TimeField(null=True)),
                ('new_remark', models.CharField(db_column='New_Remark', max_length=800, null=True)),
                ('times', models.CharField(blank=True, db_column='Times', max_length=10, null=True)),
                ('treatment_no', models.CharField(blank=True, db_column='Treatment_No', max_length=10, null=True)),
                ('workcommpoints', models.FloatField(blank=True, db_column='WorkCommPoints', default=0.0, null=True)),
                ('percent', models.FloatField(blank=True, db_column='Percent', null=True)),
                ('work_amt', models.FloatField(blank=True, db_column='Work_Amount', null=True)),
                ('session', models.FloatField(blank=True, db_column='Session', null=True)),
                ('Room_Codeid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='custom.Room')),
                ('Source_Codeid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_table.Source')),
                ('helper_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_table.Employee')),
            ],
            options={
                'db_table': 'Tmp_Item_helper',
            },
        ),
    ]