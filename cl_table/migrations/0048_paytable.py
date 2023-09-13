# Generated by Django 3.0.7 on 2023-07-17 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0047_paygroup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paytable',
            fields=[
                ('pay_code', models.CharField(blank=True, max_length=10, null=True)),
                ('pay_description', models.CharField(blank=True, max_length=50, null=True)),
                ('pay_group', models.CharField(blank=True, max_length=15, null=True)),
                ('pay_id', models.AutoField(primary_key=True, serialize=False)),
                ('pay_isactive', models.BooleanField(default=True)),
                ('gt_group', models.CharField(blank=True, choices=[('GT1', 'GT1'), ('GT2', 'GT2')], db_column='GT_Group', max_length=50, null=True)),
                ('rw_usebp', models.BooleanField(db_column='RW_useBP', null=True)),
                ('iscomm', models.BooleanField(db_column='IsComm', null=True)),
                ('show_in_report', models.BooleanField(db_column='Show_In_Report', null=True)),
                ('bank_charges', models.FloatField(blank=True, db_column='Bank_Charges', null=True)),
                ('eps', models.FloatField(blank=True, db_column='EPS', null=True)),
                ('sequence', models.IntegerField(blank=True, db_column='Sequence', null=True)),
                ('voucher_payment_control', models.BooleanField(db_column='Voucher_Payment_Control', null=True)),
                ('pay_type_pic', models.BinaryField(blank=True, db_column='PAY_TYPE_PIC', null=True)),
                ('pay_is_gst', models.BooleanField(db_column='PAY_IS_GST', null=True)),
                ('creditcardcharges', models.DecimalField(db_column='CreditCardCharges', decimal_places=2, max_digits=18, null=True)),
                ('onlinepaymentcharges', models.DecimalField(db_column='OnlinePaymentCharges', decimal_places=2, max_digits=18, null=True)),
                ('iscreditcard', models.BooleanField(blank=True, db_column='IsCreditCard', null=True)),
                ('isonlinepayment', models.BooleanField(blank=True, db_column='IsOnlinePayment', null=True)),
                ('account_code', models.CharField(blank=True, db_column='Account_Code', max_length=20, null=True)),
                ('account_mapping', models.BooleanField(blank=True, db_column='Account_Mapping', null=True)),
                ('open_cashdrawer', models.BooleanField(db_column='Open_CashDrawer', null=True)),
                ('iscustapptpromo', models.BooleanField(db_column='IsCustApptPromo', null=True)),
                ('isvoucher_extvoucher', models.BooleanField(db_column='IsVoucher_ExtVoucher', null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('pay_color', models.CharField(blank=True, max_length=255, null=True)),
                ('qr_code', models.ImageField(blank=True, null=True, upload_to='img')),
                ('paykey', models.IntegerField(blank=True, db_column='paykey', default=0, null=True)),
                ('pay_is_rounding', models.BooleanField(blank=True, db_column='Pay_Is_Rounding', default=False, null=True)),
                ('paytypeimage', models.ImageField(blank=True, null=True, upload_to='img')),
                ('pay_groupid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_table.PayGroup')),
            ],
            options={
                'db_table': 'PAYTABLE',
            },
        ),
    ]