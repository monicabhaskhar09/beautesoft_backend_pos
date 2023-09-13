# Generated by Django 3.0.7 on 2023-07-17 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0043_holditemdetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customervoucher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('customermobile', models.CharField(db_column='customerMobile', max_length=20, null=True)),
                ('firstname', models.CharField(blank=True, db_column='firstName', max_length=50, null=True)),
                ('lastname', models.CharField(blank=True, db_column='lastName', max_length=50, null=True)),
                ('outletname', models.CharField(blank=True, db_column='outletName', max_length=20, null=True)),
                ('vouchertype', models.CharField(blank=True, db_column='voucherType', max_length=200, null=True)),
                ('voucheramounttype', models.CharField(blank=True, db_column='voucherAmountType', max_length=200, null=True)),
                ('voucheramount', models.IntegerField(blank=True, db_column='voucherAmount', null=True)),
                ('promocode', models.CharField(blank=True, db_column='promoCode', max_length=20, null=True)),
                ('remarks', models.CharField(blank=True, max_length=200, null=True)),
                ('redeemdate', models.DateTimeField(blank=True, db_column='redeemDate', null=True)),
                ('cust_code', models.CharField(blank=True, max_length=20, null=True)),
                ('voucher_no', models.CharField(blank=True, max_length=20, null=True)),
                ('voucher_name', models.CharField(blank=True, max_length=20, null=True)),
                ('sitecode', models.CharField(blank=True, db_column='siteCode', max_length=10, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'CustomerVoucher',
            },
        ),
    ]
