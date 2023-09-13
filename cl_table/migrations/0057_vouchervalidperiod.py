# Generated by Django 3.0.7 on 2023-07-17 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0056_posdisc'),
    ]

    operations = [
        migrations.CreateModel(
            name='VoucherValidperiod',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('voucher_valid_code', models.CharField(db_column='Voucher_Valid_Code', max_length=20, null=True)),
                ('voucher_valid_desc', models.CharField(blank=True, db_column='Voucher_Valid_Desc', max_length=50, null=True)),
                ('voucher_valid_days', models.FloatField(blank=True, db_column='Voucher_Valid_Days', null=True)),
                ('voucher_valid_isactive', models.BooleanField(db_column='Voucher_Valid_IsActive', default=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'Voucher_ValidPeriod',
            },
        ),
    ]
