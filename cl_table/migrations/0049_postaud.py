# Generated by Django 3.0.7 on 2023-07-17 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cl_app', '0013_tmpitemhelpersession'),
        ('cl_table', '0048_paytable'),
    ]

    operations = [
        migrations.CreateModel(
            name='PosTaud',
            fields=[
                ('pay_no', models.AutoField(primary_key=True, serialize=False)),
                ('sa_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('sa_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('sa_transacno', models.CharField(blank=True, max_length=20, null=True)),
                ('pay_group', models.CharField(blank=True, max_length=40, null=True)),
                ('pay_type', models.CharField(blank=True, max_length=30, null=True)),
                ('pay_desc', models.CharField(blank=True, db_column='pay_Desc', max_length=200, null=True)),
                ('pay_tendamt', models.FloatField(blank=True, null=True)),
                ('pay_tendrate', models.FloatField(blank=True, null=True)),
                ('pay_tendcurr', models.CharField(blank=True, max_length=10, null=True)),
                ('pay_amt', models.FloatField(blank=True, null=True)),
                ('pay_amtrate', models.FloatField(blank=True, null=True)),
                ('pay_amtcurr', models.CharField(blank=True, max_length=10, null=True)),
                ('pay_rem1', models.CharField(blank=True, max_length=200, null=True)),
                ('pay_rem2', models.CharField(blank=True, max_length=200, null=True)),
                ('pay_rem3', models.CharField(blank=True, max_length=200, null=True)),
                ('pay_rem4', models.CharField(blank=True, max_length=200, null=True)),
                ('pay_status', models.BooleanField(blank=True, null=True)),
                ('pay_actamt', models.FloatField(blank=True, null=True)),
                ('itemsite_code', models.CharField(db_column='ItemSIte_Code', max_length=10, null=True)),
                ('paychange', models.FloatField(blank=True, db_column='PayChange', null=True)),
                ('dt_lineno', models.IntegerField(null=True)),
                ('pay_gst_amt_collect', models.FloatField(blank=True, db_column='Pay_GST_Amt_Collect', null=True)),
                ('pay_gst', models.FloatField(blank=True, db_column='PAY_GST', null=True)),
                ('posdaudlineno', models.CharField(blank=True, db_column='POSDAUDLineNo', max_length=50, null=True)),
                ('subtotal', models.FloatField(null=True)),
                ('tax', models.FloatField(null=True)),
                ('discount_amt', models.FloatField(null=True)),
                ('billable_amount', models.FloatField(null=True)),
                ('credit_debit', models.BooleanField(default=False, null=True)),
                ('points', models.BooleanField(default=False, null=True)),
                ('prepaid', models.BooleanField(default=False, null=True)),
                ('pay_premise', models.BooleanField(default=False, null=True)),
                ('is_voucher', models.BooleanField(default=False, null=True)),
                ('ItemSIte_Codeid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_app.ItemSitelist')),
                ('billed_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_table.Fmspw')),
                ('pay_groupid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_table.PayGroup')),
                ('pay_typeid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_table.Paytable')),
            ],
            options={
                'db_table': 'pos_taud',
            },
        ),
    ]
