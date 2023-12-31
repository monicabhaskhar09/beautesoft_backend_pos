# Generated by Django 3.0.7 on 2023-07-17 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cl_app', '0013_tmpitemhelpersession'),
        ('custom', '0008_auto_20230717_1317'),
        ('cl_table', '0045_poshaud'),
    ]

    operations = [
        migrations.CreateModel(
            name='PosDaud',
            fields=[
                ('dt_no', models.AutoField(primary_key=True, serialize=False)),
                ('sa_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('sa_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('sa_transacno', models.CharField(blank=True, max_length=20, null=True)),
                ('dt_status', models.CharField(blank=True, choices=[('SA', 'SA'), ('VT', 'VT'), ('SU', 'SU'), ('EX', 'EX')], max_length=5, null=True)),
                ('dt_itemno', models.CharField(blank=True, max_length=20, null=True)),
                ('dt_itemdesc', models.CharField(blank=True, max_length=200, null=True)),
                ('dt_price', models.FloatField(blank=True, null=True)),
                ('dt_promoprice', models.FloatField(blank=True, db_column='dt_PromoPrice', null=True)),
                ('dt_amt', models.FloatField(blank=True, null=True)),
                ('dt_qty', models.IntegerField(blank=True, null=True)),
                ('dt_discamt', models.FloatField(blank=True, db_column='dt_discAmt', null=True)),
                ('dt_discpercent', models.FloatField(blank=True, db_column='dt_discPercent', null=True)),
                ('dt_discdesc', models.CharField(blank=True, db_column='dt_discDesc', max_length=200, null=True)),
                ('dt_discno', models.CharField(blank=True, max_length=10, null=True)),
                ('dt_remark', models.CharField(blank=True, max_length=60, null=True)),
                ('dt_staffno', models.CharField(blank=True, db_column='dt_Staffno', max_length=100, null=True)),
                ('dt_staffname', models.CharField(blank=True, db_column='dt_StaffName', max_length=600, null=True)),
                ('dt_discuser', models.CharField(blank=True, db_column='dt_DiscUser', max_length=50, null=True)),
                ('dt_combocode', models.CharField(blank=True, db_column='dt_ComboCode', max_length=20, null=True)),
                ('itemsite_code', models.CharField(blank=True, db_column='ItemSite_Code', max_length=10, null=True)),
                ('dt_lineno', models.IntegerField(blank=True, db_column='dt_LineNo', null=True)),
                ('dt_uom', models.CharField(blank=True, db_column='dt_UOM', max_length=20, null=True)),
                ('isfoc', models.BooleanField(blank=True, db_column='IsFoc', null=True)),
                ('item_remarks', models.CharField(blank=True, db_column='Item_Remarks', max_length=500, null=True)),
                ('dt_transacamt', models.FloatField(blank=True, db_column='dt_TransacAmt', null=True)),
                ('dt_deposit', models.FloatField(blank=True, null=True)),
                ('holditemqty', models.IntegerField(blank=True, db_column='HoldItemQty', null=True)),
                ('st_ref_treatmentcode', models.CharField(blank=True, db_column='ST_Ref_TreatmentCode', max_length=500, null=True)),
                ('item_status_code', models.CharField(blank=True, db_column='Item_Status_Code', max_length=50, null=True)),
                ('first_trmt_done', models.BooleanField(blank=True, db_column='First_Trmt_Done', null=True)),
                ('first_trmt_done_staff_code', models.CharField(blank=True, db_column='First_Trmt_Done_Staff_Code', max_length=200, null=True)),
                ('first_trmt_done_staff_name', models.CharField(blank=True, db_column='First_Trmt_Done_Staff_Name', max_length=200, null=True)),
                ('record_detail_type', models.CharField(blank=True, choices=[('SERVICE', 'SERVICE'), ('PRODUCT', 'PRODUCT'), ('PREPAID', 'PREPAID'), ('VOUCHER', 'VOUCHER'), ('PACKAGE', 'PACKAGE'), ('TD', 'TD'), ('TP SERVICE', 'TP SERVICE'), ('TP PRODUCT', 'TP PRODUCT'), ('TP PREPAID', 'TP PREPAID')], db_column='Record_Detail_Type', max_length=50, null=True)),
                ('trmt_done_staff_code', models.CharField(blank=True, db_column='Trmt_Done_Staff_Code', max_length=200, null=True)),
                ('trmt_done_staff_name', models.CharField(blank=True, db_column='Trmt_Done_Staff_Name', max_length=200, null=True)),
                ('trmt_done_id', models.CharField(blank=True, db_column='Trmt_Done_ID', max_length=50, null=True)),
                ('trmt_done_type', models.CharField(blank=True, db_column='Trmt_Done_Type', max_length=50, null=True)),
                ('topup_service_trmt_code', models.CharField(blank=True, db_column='TopUp_Service_Trmt_Code', max_length=50, null=True)),
                ('topup_product_treat_code', models.CharField(blank=True, db_column='TopUp_Product_Treat_Code', max_length=50, null=True)),
                ('topup_prepaid_trans_code', models.CharField(blank=True, db_column='TopUp_Prepaid_Trans_Code', max_length=50, null=True)),
                ('topup_prepaid_type_code', models.CharField(blank=True, db_column='TopUp_Prepaid_Type_Code', max_length=50, null=True)),
                ('gst_amt_collect', models.FloatField(blank=True, db_column='GST_Amt_Collect', null=True)),
                ('topup_prepaid_pos_trans_lineno', models.IntegerField(blank=True, db_column='TopUp_Prepaid_POS_Trans_LineNo', null=True)),
                ('topup_outstanding', models.FloatField(blank=True, db_column='TopUp_Outstanding', null=True)),
                ('staffs', models.CharField(db_column='Staffs', max_length=300, null=True)),
                ('ItemSite_Codeid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_app.ItemSitelist')),
                ('dt_Staffnoid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_table.Employee')),
                ('dt_itemnoid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_table.Stock')),
                ('itemcart', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='custom.ItemCart')),
            ],
            options={
                'db_table': 'pos_daud',
            },
        ),
    ]
