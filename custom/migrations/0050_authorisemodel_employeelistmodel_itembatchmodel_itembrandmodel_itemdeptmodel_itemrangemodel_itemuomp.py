# Generated by Django 3.0.7 on 2023-07-17 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0049_dodetailmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthoriseModel',
            fields=[
                ('PW_ID', models.AutoField(db_column='PW_ID', primary_key=True, serialize=False)),
                ('PW_UserLogin', models.CharField(blank=True, db_column='PW_UserLogin', max_length=255, null=True)),
                ('flgdisc', models.IntegerField(blank=True, db_column='flgdisc', null=True)),
                ('LEVEL_ItmID', models.IntegerField(blank=True, db_column='LEVEL_ItmID', null=True)),
                ('Level_Desc', models.CharField(blank=True, db_column='Level_Desc', max_length=255, null=True)),
                ('Emp_Code', models.CharField(blank=True, db_column='Emp_Code', max_length=255, null=True)),
                ('flgPHY', models.IntegerField(blank=True, db_column='flgPHY', null=True)),
                ('flgGRN', models.IntegerField(blank=True, db_column='flgGRN', null=True)),
                ('flgADJ', models.IntegerField(blank=True, db_column='flgADJ', null=True)),
                ('flgTFR', models.IntegerField(blank=True, db_column='flgTFR', null=True)),
                ('flgStockUsageMemo', models.IntegerField(blank=True, db_column='flgStockUsageMemo', default=1, null=True)),
                ('flgDelArt', models.IntegerField(blank=True, db_column='flgDelArt', null=True)),
                ('flgMClock', models.IntegerField(blank=True, db_column='flgMClock', null=True)),
                ('lallowFlgDelArt', models.IntegerField(blank=True, db_column='lallowFlgDelArt', null=True)),
                ('flgopendrawer', models.IntegerField(blank=True, db_column='flgopendrawer', null=True)),
                ('flgExchange', models.IntegerField(blank=True, db_column='flgExchange', null=True)),
                ('flgRevTrm', models.IntegerField(blank=True, db_column='flgRevTrm', null=True)),
                ('flgVoid', models.IntegerField(blank=True, db_column='flgVoid', null=True)),
                ('flgRefund', models.IntegerField(blank=True, db_column='flgRefund', null=True)),
                ('flgEmail', models.IntegerField(blank=True, db_column='flgEmail', null=True)),
                ('flgCustAdd', models.IntegerField(blank=True, db_column='flgCustAdd', null=True)),
                ('flgViewCost', models.IntegerField(blank=True, db_column='flgViewCost', null=True)),
                ('flgFOC', models.IntegerField(blank=True, db_column='flgFOC', null=True)),
                ('flgAppt', models.IntegerField(blank=True, db_column='flgAppt', null=True)),
                ('flgExpire', models.IntegerField(blank=True, db_column='flgExpire', null=True)),
                ('flgViewAth', models.IntegerField(blank=True, db_column='flgViewAth', null=True)),
                ('flgAddAth', models.IntegerField(blank=True, db_column='flgAddAth', null=True)),
                ('flgEditAth', models.IntegerField(blank=True, db_column='flgEditAth', null=True)),
                ('flgRefundPP', models.IntegerField(blank=True, db_column='flgRefundPP', null=True)),
                ('flgRefundCN', models.IntegerField(blank=True, db_column='flgRefundCN', null=True)),
                ('flgAttn', models.IntegerField(blank=True, db_column='flgAttn', null=True)),
                ('flgChangeExpiryDate', models.IntegerField(blank=True, db_column='flgChangeExpiryDate', null=True)),
                ('flgOutletRequest', models.IntegerField(blank=True, db_column='flgOutletRequest', null=True)),
                ('flgApptEditAth', models.IntegerField(blank=True, db_column='flgApptEditAth', null=True)),
                ('flgChangeUnitPrice', models.IntegerField(blank=True, db_column='flgChangeUnitPrice', null=True)),
                ('flgLuckyDraw', models.IntegerField(blank=True, db_column='flgLuckyDraw', null=True)),
                ('flgOverideARStaff', models.IntegerField(blank=True, db_column='flgOverideARStaff', null=True)),
                ('flgAccountInterface', models.IntegerField(blank=True, db_column='flgAccountInterface', null=True)),
                ('flgVoidCurrentDay', models.IntegerField(blank=True, db_column='flgVoidCurrentDay', null=True)),
                ('flgAllCom', models.IntegerField(blank=True, db_column='flgAllCom', null=True)),
                ('flgAllowInsufficent', models.IntegerField(blank=True, db_column='flgAllowInsufficent', null=True)),
                ('flgAllowCardUsage', models.IntegerField(blank=True, db_column='flgAllowCardUsage', null=True)),
                ('flgAllowBlockAppointment', models.IntegerField(blank=True, db_column='flgAllowBlockAppointment', null=True)),
                ('flgAllowTDExpiryService', models.IntegerField(blank=True, db_column='flgAllowTDExpiryService', null=True)),
                ('flgAllDayEndSettlement', models.IntegerField(blank=True, db_column='flgAllDayEndSettlement', null=True)),
                ('LEVEL_ItmIDid_id', models.IntegerField(blank=True, db_column='LEVEL_ItmIDid_id', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='created_at', null=True)),
                ('flgCallDateChange', models.IntegerField(blank=True, db_column='flgCallDateChange', null=True)),
                ('flgCallModule', models.IntegerField(blank=True, db_column='flgCallModule', null=True)),
                ('flgGiftModule', models.IntegerField(blank=True, db_column='flgGiftModule', null=True)),
                ('flgHMSetting', models.IntegerField(blank=True, db_column='flgHMSetting', null=True)),
                ('flgSales', models.IntegerField(blank=True, db_column='flgSales', null=True)),
                ('loginsite_id', models.IntegerField(blank=True, db_column='loginsite_id', null=True)),
                ('PW_Isactive', models.IntegerField(blank=True, db_column='PW_Isactive', default=1, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_column='updated_at', null=True)),
                ('user_id', models.IntegerField(blank=True, db_column='user_id', null=True)),
                ('Emp_Codeid_id', models.IntegerField(blank=True, db_column='Emp_Codeid_id', null=True)),
                ('is_reversal', models.BooleanField(db_column='Reversal', default=False)),
            ],
            options={
                'db_table': 'FMSPW',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EmployeeListModel',
            fields=[
                ('Emp_no', models.AutoField(db_column='Emp_no', primary_key=True, serialize=False)),
                ('Emp_code', models.CharField(blank=True, db_column='Emp_code', max_length=255, null=True)),
                ('Emp_name', models.CharField(blank=True, db_column='Emp_name', max_length=255, null=True)),
            ],
            options={
                'db_table': 'Employee',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ItemBatchModel',
            fields=[
                ('ID', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('ITEM_CODE', models.CharField(blank=True, db_column='ITEM_CODE', default='', max_length=255, null=True)),
                ('SITE_CODE', models.CharField(blank=True, db_column='SITE_CODE', default='', max_length=255, null=True)),
                ('BATCH_NO', models.CharField(blank=True, db_column='BATCH_NO', default='', max_length=255, null=True)),
                ('UOM', models.CharField(blank=True, db_column='UOM', default='', max_length=255, null=True)),
                ('QTY', models.FloatField(blank=True, db_column='QTY', null=True)),
                ('EXP_DATE', models.DateTimeField(db_column='EXP_DATE', null=True)),
                ('BATCH_COST', models.FloatField(blank=True, db_column='BATCH_COST', null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_column='updated_at', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='created_at', null=True)),
                ('IsActive', models.IntegerField(blank=True, db_column='IsActive', default=1, null=True)),
            ],
            options={
                'db_table': 'ITEM_BATCH',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ItemBrandModel',
            fields=[
                ('itm_id', models.AutoField(db_column='itm_id', primary_key=True, serialize=False)),
                ('itm_code', models.IntegerField(blank=True, db_column='itm_code', null=True)),
                ('itm_desc', models.CharField(blank=True, db_column='itm_desc', max_length=255, null=True)),
                ('itm_status', models.IntegerField(blank=True, db_column='itm_status', null=True)),
                ('ITM_SEQ', models.CharField(blank=True, db_column='ITM_SEQ', max_length=255, null=True)),
                ('PIC_PATH', models.CharField(blank=True, db_column='PIC_PATH', max_length=255, null=True)),
                ('Voucher_For_Sales', models.IntegerField(blank=True, db_column='Voucher_For_Sales', default=1, null=True)),
                ('Voucher_Brand', models.IntegerField(blank=True, db_column='Voucher_Brand', default=1, null=True)),
                ('Retail_Product_Brand', models.IntegerField(blank=True, db_column='Retail_Product_Brand', default=1, null=True)),
                ('Prepaid_Brand', models.IntegerField(blank=True, db_column='Prepaid_Brand', default=1, null=True)),
                ('Process_Remark', models.CharField(blank=True, db_column='Process_Remark', max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='created_at', null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_column='updated_at', null=True)),
            ],
            options={
                'db_table': 'Item_Brand',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ItemDeptModel',
            fields=[
                ('itm_id', models.AutoField(db_column='itm_id', primary_key=True, serialize=False)),
                ('itm_code', models.CharField(blank=True, max_length=10, null=True)),
                ('itm_desc', models.CharField(blank=True, max_length=40, null=True)),
                ('itm_status', models.BooleanField(default=True)),
                ('itm_seq', models.IntegerField(blank=True, db_column='ITM_SEQ', null=True)),
                ('process_remark', models.CharField(blank=True, db_column='Process_Remark', max_length=250, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'Item_Dept',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ItemRangeModel',
            fields=[
                ('itm_id', models.AutoField(db_column='itm_id', primary_key=True, serialize=False)),
                ('itm_code', models.IntegerField(blank=True, db_column='itm_code', null=True)),
                ('itm_desc', models.CharField(blank=True, db_column='itm_desc', max_length=255, null=True)),
                ('itm_status', models.IntegerField(blank=True, db_column='itm_status', null=True)),
                ('ITM_SEQ', models.CharField(blank=True, db_column='ITM_SEQ', max_length=255, null=True)),
                ('itm_brand', models.CharField(blank=True, db_column='itm_brand', max_length=255, null=True)),
                ('itm_Dept', models.CharField(blank=True, db_column='itm_Dept', max_length=255, null=True)),
                ('isProduct', models.IntegerField(blank=True, db_column='isProduct', null=True)),
                ('PIC_PATH', models.CharField(blank=True, db_column='PIC_PATH', max_length=255, null=True)),
                ('Prepaid_For_Product', models.IntegerField(blank=True, db_column='Prepaid_For_Product', default=1, null=True)),
                ('Prepaid_For_Service', models.IntegerField(blank=True, db_column='Prepaid_For_Service', default=1, null=True)),
                ('Prepaid_For_All', models.IntegerField(blank=True, db_column='Prepaid_For_All', default=1, null=True)),
                ('IsService', models.IntegerField(blank=True, db_column='IsService', default=1, null=True)),
                ('IsVoucher', models.IntegerField(blank=True, db_column='IsVoucher', default=1, null=True)),
                ('IsPrepaid', models.IntegerField(blank=True, db_column='IsPrepaid', default=1, null=True)),
                ('IsCompound', models.IntegerField(blank=True, db_column='IsCompound', default=1, null=True)),
                ('Process_Remark', models.CharField(blank=True, db_column='Process_Remark', max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='created_at', null=True)),
                ('itm_Deptid_id', models.IntegerField(blank=True, db_column='itm_Deptid_id', default=1, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_column='updated_at', null=True)),
            ],
            options={
                'db_table': 'Item_Range',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ItemUOMPriceModel',
            fields=[
                ('ID', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('ITEM_CODE', models.CharField(blank=True, db_column='ITEM_CODE', default='', max_length=255, null=True)),
                ('ITEM_UOM', models.CharField(blank=True, db_column='ITEM_UOM', default='', max_length=255, null=True)),
                ('UOM_DESC', models.CharField(blank=True, db_column='UOM_DESC', default='', max_length=255, null=True)),
                ('UOM_UNIT', models.FloatField(blank=True, db_column='UOM_UNIT', null=True)),
                ('ITEM_UOM2', models.CharField(blank=True, db_column='ITEM_UOM2', default='', max_length=255, null=True)),
                ('UOM2_DESC', models.CharField(blank=True, db_column='UOM2_DESC', default='', max_length=255, null=True)),
                ('ITEM_PRICE', models.FloatField(blank=True, db_column='ITEM_PRICE', null=True)),
                ('ITEM_COST', models.FloatField(blank=True, db_column='ITEM_COST', null=True)),
                ('MIN_MARGIN', models.FloatField(blank=True, db_column='MIN_MARGIN', null=True)),
                ('IsActive', models.IntegerField(blank=True, db_column='IsActive', default=1, null=True)),
                ('Item_UOMPrice_SEQ', models.FloatField(blank=True, db_column='Item_UOMPrice_SEQ', null=True)),
                ('Delete_User', models.CharField(blank=True, db_column='Delete_User', default='', max_length=255, null=True)),
                ('Delete_DATE', models.DateTimeField(db_column='Delete_DATE', null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_column='updated_at', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='created_at', null=True)),
            ],
            options={
                'db_table': 'ITEM_UOMPRICE',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SiteCodeModel',
            fields=[
                ('ItemSite_ID', models.AutoField(db_column='ItemSite_ID', primary_key=True, serialize=False)),
                ('ItemSite_Code', models.CharField(blank=True, db_column='ItemSite_Code', default='', max_length=255, null=True)),
                ('ItemSite_Desc', models.CharField(blank=True, db_column='ItemSite_Desc', default='', max_length=255, null=True)),
                ('ItemSite_Type', models.CharField(blank=True, db_column='ItemSite_Type', default='', max_length=255, null=True)),
                ('Item_PurchaseDept', models.CharField(blank=True, db_column='Item_PurchaseDept', default='', max_length=255, null=True)),
                ('ItemSite_Address', models.CharField(blank=True, db_column='ItemSite_Address', default='', max_length=255, null=True)),
                ('ItemSite_Postcode', models.CharField(blank=True, db_column='ItemSite_Postcode', default='', max_length=255, null=True)),
                ('ItemSite_City', models.CharField(blank=True, db_column='ItemSite_City', default='', max_length=255, null=True)),
                ('ItemSite_State', models.CharField(blank=True, db_column='ItemSite_State', default='', max_length=255, null=True)),
                ('ItemSite_Country', models.CharField(blank=True, db_column='ItemSite_Country', default='', max_length=255, null=True)),
                ('ItemSite_Phone1', models.CharField(blank=True, db_column='ItemSite_Phone1', default='', max_length=255, null=True)),
                ('ItemSite_Phone2', models.CharField(blank=True, db_column='ItemSite_Phone2', default='', max_length=255, null=True)),
                ('ItemSite_Fax', models.CharField(blank=True, db_column='ItemSite_Fax', default='', max_length=255, null=True)),
                ('ItemSite_Email', models.CharField(blank=True, db_column='ItemSite_Email', default='', max_length=255, null=True)),
                ('ItemSite_User', models.CharField(blank=True, db_column='ItemSite_User', default='', max_length=255, null=True)),
                ('ItemSite_Date', models.DateField(db_column='ItemSite_Date', null=True)),
                ('ItemSite_Time', models.DateTimeField(db_column='ItemSite_Time', null=True)),
                ('ItemSite_Isactive', models.IntegerField(blank=True, db_column='ItemSite_Isactive', null=True)),
                ('ITEMSITE_REFCODE', models.CharField(blank=True, db_column='ITEMSITE_REFCODE', default='', max_length=255, null=True)),
                ('Site_Group', models.CharField(blank=True, db_column='Site_Group', default='', max_length=255, null=True)),
                ('site_is_gst', models.BooleanField(db_column='SITE_IS_GST', default=False, null=True)),
                ('Account_Code', models.CharField(blank=True, db_column='Account_Code', default='', max_length=255, null=True)),
                ('ClientIndex', models.IntegerField(blank=True, db_column='ClientIndex', null=True)),
                ('HeartBeat', models.DateTimeField(db_column='HeartBeat', null=True)),
                ('SystemLog_MDPL_Update', models.IntegerField(blank=True, db_column='SystemLog_MDPL_Update', null=True)),
                ('geolink', models.CharField(blank=True, db_column='geolink', default='', max_length=255, null=True)),
                ('weekdays_timing', models.CharField(blank=True, db_column='weekdays_timing', default='', max_length=255, null=True)),
                ('weekend_timing', models.CharField(blank=True, db_column='weekend_timing', default='', max_length=255, null=True)),
                ('holliday_timing', models.CharField(blank=True, db_column='holliday_timing', default='', max_length=255, null=True)),
                ('Closed_on', models.CharField(blank=True, db_column='Closed_on', default='', max_length=255, null=True)),
                ('picpath', models.CharField(blank=True, db_column='picpath', default='', max_length=255, null=True)),
                ('Owner', models.CharField(blank=True, db_column='Owner', default='', max_length=255, null=True)),
                ('Site_Groupid_id', models.IntegerField(blank=True, db_column='Site_Groupid_id', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='created_at', null=True)),
                ('pic_Path', models.CharField(blank=True, db_column='pic_Path', default='', max_length=255, null=True)),
                ('QRCode', models.CharField(blank=True, db_column='QRCode', default='', max_length=255, null=True)),
                ('Ratings', models.CharField(blank=True, db_column='Ratings', default='', max_length=255, null=True)),
                ('siteDbConnectionUrl', models.CharField(blank=True, db_column='siteDbConnectionUrl', default='', max_length=255, null=True)),
                ('skills_list', models.CharField(blank=True, db_column='skills_list', default='', max_length=255, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_column='updated_at', null=True)),
                ('ItemSite_Cityid_id', models.IntegerField(blank=True, db_column='ItemSite_Cityid_id', null=True)),
                ('ItemSite_Countryid_id', models.IntegerField(blank=True, db_column='ItemSite_Countryid_id', null=True)),
                ('ItemSite_Stateid_id', models.IntegerField(blank=True, db_column='ItemSite_Stateid_id', null=True)),
                ('ItemSite_Userid_id', models.IntegerField(blank=True, db_column='ItemSite_Userid_id', null=True)),
                ('is_nric', models.IntegerField(blank=True, db_column='Nric', null=True)),
                ('is_automember', models.IntegerField(blank=True, db_column='IsAutoMember', null=True)),
                ('Invoice_TemplateName', models.CharField(blank=True, db_column='Invoice_TemplateName', default='', max_length=255, null=True)),
                ('resource_count', models.CharField(blank=True, db_column='resource_count', default='', max_length=255, null=True)),
                ('cell_duration', models.CharField(blank=True, db_column='Cell_Duration', default='', max_length=255, null=True)),
                ('EndDay_Hour', models.CharField(blank=True, db_column='EndDay_Hour', default='', max_length=255, null=True)),
                ('StartDay_Hour', models.CharField(blank=True, db_column='StartDay_Hour', default='', max_length=255, null=True)),
                ('url', models.CharField(blank=True, db_column='url', default='', max_length=255, null=True)),
                ('is_dragappt', models.IntegerField(blank=True, db_column='is_dragappt', null=True)),
                ('is_empvalidate', models.IntegerField(blank=True, db_column='is_empvalidate', null=True)),
            ],
            options={
                'db_table': 'Item_SiteList',
                'managed': False,
            },
        ),
    ]
