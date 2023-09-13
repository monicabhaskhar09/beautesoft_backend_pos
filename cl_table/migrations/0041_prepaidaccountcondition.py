# Generated by Django 3.0.7 on 2023-07-17 13:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0040_depositaccount'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrepaidAccountCondition',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('pp_no', models.CharField(db_column='PP_NO', max_length=50, null=True)),
                ('pp_type', models.CharField(db_column='PP_TYPE', max_length=50, null=True)),
                ('pp_desc', models.CharField(blank=True, db_column='PP_DESC', max_length=250, null=True)),
                ('p_itemtype', models.CharField(db_column='P_ItemType', max_length=50, null=True)),
                ('item_code', models.CharField(max_length=20, null=True)),
                ('conditiontype1', models.CharField(db_column='ConditionType1', max_length=80, null=True)),
                ('conditiontype2', models.CharField(db_column='ConditionType2', max_length=80, null=True)),
                ('amount', models.DecimalField(blank=True, db_column='Amount', decimal_places=4, max_digits=19, null=True)),
                ('rate', models.CharField(blank=True, db_column='Rate', max_length=20, null=True)),
                ('membercardnoaccess', models.BooleanField(db_column='MemberCardNoAccess', null=True)),
                ('use_amt', models.FloatField(blank=True, db_column='Use_Amt', null=True)),
                ('remain', models.FloatField(blank=True, db_column='Remain', null=True)),
                ('pos_daud_lineno', models.FloatField(db_column='POS_Daud_LineNo', null=True)),
                ('system_remark', models.CharField(blank=True, db_column='System_Remark', max_length=100, null=True)),
                ('lpackage', models.BooleanField(db_column='lPackage', null=True)),
                ('package_code', models.CharField(blank=True, db_column='Package_Code', max_length=50, null=True)),
                ('package_code_lineno', models.IntegerField(blank=True, db_column='Package_Code_LineNo', null=True)),
                ('creditvalueshared', models.BooleanField(db_column='CreditValueShared', null=True)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('itemdept_id', models.IntegerField(blank=True, db_column='itemdept_id', null=True)),
                ('itembrand_id', models.IntegerField(blank=True, db_column='itembrand_id', null=True)),
            ],
            options={
                'db_table': 'Prepaid_Account_Condition',
            },
        ),
    ]