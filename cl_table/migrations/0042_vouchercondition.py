# Generated by Django 3.0.7 on 2023-07-17 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0041_prepaidaccountcondition'),
    ]

    operations = [
        migrations.CreateModel(
            name='VoucherCondition',
            fields=[
                ('itemid', models.AutoField(db_column='ItemID', primary_key=True, serialize=False)),
                ('p_itemtype', models.CharField(blank=True, db_column='P_ItemType', max_length=14, null=True)),
                ('item_code', models.CharField(blank=True, max_length=20, null=True)),
                ('conditiontype1', models.CharField(blank=True, db_column='ConditionType1', max_length=20, null=True)),
                ('conditiontype2', models.CharField(blank=True, db_column='ConditionType2', max_length=20, null=True)),
                ('amount', models.DecimalField(blank=True, db_column='Amount', decimal_places=4, max_digits=19, null=True)),
                ('rate', models.CharField(blank=True, db_column='Rate', max_length=10, null=True)),
                ('membercardnoaccess', models.BooleanField(blank=True, db_column='MemberCardNoAccess', null=True)),
                ('line_no', models.IntegerField(blank=True, db_column='Line_No', null=True)),
                ('isactive', models.BooleanField(db_column='IsActive', default=True)),
            ],
            options={
                'db_table': 'Voucher_condition',
            },
        ),
    ]