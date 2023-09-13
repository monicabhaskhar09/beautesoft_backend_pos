# Generated by Django 3.0.7 on 2023-07-17 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0049_postaud'),
    ]

    operations = [
        migrations.CreateModel(
            name='DepositType',
            fields=[
                ('sys_id', models.AutoField(db_column='Sys_ID', primary_key=True, serialize=False)),
                ('sa_transacno', models.CharField(max_length=20, null=True)),
                ('pay_group', models.CharField(blank=True, db_column='Pay_Group', max_length=50, null=True)),
                ('pay_type', models.CharField(blank=True, db_column='Pay_Type', max_length=30, null=True)),
                ('amount', models.FloatField(blank=True, db_column='Amount', null=True)),
                ('card_no', models.CharField(max_length=200, null=True)),
                ('pay_desc', models.CharField(max_length=100, null=True)),
                ('pay_tendcurr', models.CharField(blank=True, max_length=10, null=True)),
                ('pay_tendrate', models.FloatField(blank=True, null=True)),
                ('site_code', models.CharField(blank=True, db_column='Site_Code', max_length=50, null=True)),
                ('pos_taud_lineno', models.IntegerField(db_column='POS_TAUD_LineNo', null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'Deposit_Type',
            },
        ),
    ]