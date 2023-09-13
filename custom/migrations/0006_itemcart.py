# Generated by Django 3.0.7 on 2023-07-17 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cl_app', '0013_tmpitemhelpersession'),
        ('cl_table', '0027_focreason'),
        ('custom', '0005_voucherrecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemCart',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('phonenumber', models.CharField(blank=True, db_column='phoneNumber', max_length=255, null=True)),
                ('customercode', models.CharField(blank=True, db_column='customerCode', max_length=50, null=True)),
                ('itemcode', models.CharField(blank=True, db_column='itemCode', max_length=50, null=True)),
                ('itemdesc', models.CharField(blank=True, db_column='itemDesc', max_length=500, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=18, null=True)),
                ('sitecode', models.CharField(blank=True, db_column='siteCode', max_length=20, null=True)),
                ('isactive', models.BooleanField(blank=True, db_column='isActive', default=True, null=True)),
                ('timstamp', models.DateTimeField(blank=True, db_column='timStamp', null=True)),
                ('redeempoint', models.FloatField(blank=True, db_column='redeemPoint', null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('discount', models.FloatField(default=0.0, null=True)),
                ('discount_amt', models.FloatField(default=0.0, null=True)),
                ('discount_price', models.FloatField(default=0.0, null=True)),
                ('tax', models.FloatField(null=True)),
                ('is_payment', models.BooleanField(default=False, null=True)),
                ('additional_discount', models.FloatField(default=0.0, null=True)),
                ('additional_discountamt', models.FloatField(default=0.0, null=True)),
                ('deposit', models.FloatField(default=0.0, null=True)),
                ('total_price', models.FloatField(default=0.0, null=True)),
                ('trans_amt', models.FloatField(default=0.0, null=True)),
                ('cart_id', models.CharField(max_length=20, null=True)),
                ('cart_date', models.DateField(db_column='Cart_Date', null=True)),
                ('cart_status', models.CharField(choices=[('Inprogress', 'Inprogress'), ('Suspension', 'Suspension'), ('Completed', 'Completed')], db_column='Cart_Status', default='Inprogress', max_length=20)),
                ('lineno', models.IntegerField(db_column='LineNo', null=True)),
                ('check', models.CharField(choices=[('New', 'New'), ('Old', 'Old')], db_column='Check', max_length=20, null=True)),
                ('ratio', models.DecimalField(db_column='Ratio', decimal_places=15, max_digits=18, null=True)),
                ('sa_transacno', models.CharField(max_length=20, null=True)),
                ('remark', models.CharField(db_column='Remark', max_length=500, null=True)),
                ('discreason_txt', models.CharField(max_length=500, null=True)),
                ('holditemqty', models.IntegerField(db_column='HoldItemQty', null=True)),
                ('auto', models.BooleanField(default=True)),
                ('done_sessions', models.CharField(blank=True, db_column='Done_Sessions', max_length=700, null=True)),
                ('type', models.CharField(blank=True, choices=[('Deposit', 'Deposit'), ('Top Up', 'Top Up'), ('Sales', 'Sales'), ('VT-Deposit', 'VT-Deposit'), ('VT-Top Up', 'VT-Top Up'), ('VT-Sales', 'VT-Sales'), ('Exchange', 'Exchange')], db_column='Type', max_length=10, null=True)),
                ('is_foc', models.BooleanField(default=False)),
                ('recorddetail', models.CharField(max_length=20, null=True)),
                ('itemtype', models.CharField(max_length=20, null=True)),
                ('treatment_no', models.CharField(blank=True, db_column='Treatment_No', max_length=10, null=True)),
                ('free_sessions', models.CharField(blank=True, db_column='Free_Sessions', max_length=10, null=True)),
                ('is_total', models.BooleanField(default=False, null=True)),
                ('prepaid_value', models.FloatField(blank=True, db_column='Prepaid_Value', null=True)),
                ('isopen_prepaid', models.BooleanField(db_column='isOpen_Prepaid', default=False)),
                ('sessiondone', models.CharField(blank=True, db_column='Session_Done', max_length=700, null=True)),
                ('is_service', models.BooleanField(default=False, null=True)),
                ('treat_expiry', models.DateField(blank=True, db_column='Treatment_Expiry', null=True)),
                ('treat_type', models.CharField(blank=True, db_column='treat_type', max_length=50, null=True)),
                ('treatment_limit_times', models.FloatField(blank=True, db_column='Treatment_Limit_Times', null=True)),
                ('is_flexi', models.BooleanField(blank=True, default=False, null=True)),
                ('is_flexinewservice', models.BooleanField(blank=True, default=False, null=True)),
                ('addstaff_time', models.IntegerField(blank=True, null=True)),
                ('batch_sno', models.CharField(blank=True, db_column='BATCH_SNO', max_length=30, null=True)),
                ('Appointment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_table.Appointment')),
                ('cust_noid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_table.Customer')),
                ('disc_reason', models.ManyToManyField(blank=True, to='custom.PaymentRemarks')),
                ('focreason', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_table.FocReason')),
                ('helper_ids', models.ManyToManyField(blank=True, related_name='itemhelper', to='cl_table.TmpItemHelper')),
                ('holdreason', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='custom.HolditemSetup')),
                ('item_uom', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_table.ItemUom')),
                ('itemcodeid', models.ForeignKey(db_column='itemCodeid', null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_table.Stock')),
                ('itemstatus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_table.ItemStatus')),
                ('multi_treat', models.ManyToManyField(blank=True, to='cl_table.Treatment')),
                ('products_used', models.ManyToManyField(blank=True, related_name='salon_product', to='cl_table.Stock')),
                ('sales_staff', models.ManyToManyField(blank=True, related_name='sales_staff', to='cl_table.Employee')),
                ('service_staff', models.ManyToManyField(blank=True, related_name='service_staff', to='cl_table.Employee')),
                ('sitecodeid', models.ForeignKey(db_column='sitecodeid', null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_app.ItemSitelist')),
                ('treatment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Treatment', to='cl_table.Treatment')),
                ('treatment_account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='trmtacc', to='cl_table.TreatmentAccount')),
            ],
            options={
                'db_table': 'item_Cart',
            },
        ),
    ]