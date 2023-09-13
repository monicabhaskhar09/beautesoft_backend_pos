# Generated by Django 3.0.7 on 2023-07-17 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_app', '0008_usagelevel'),
    ]

    operations = [
        migrations.CreateModel(
            name='priceChangeLog',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('sa_transacno', models.CharField(blank=True, max_length=20, null=True)),
                ('itemsite_code', models.CharField(blank=True, db_column='ItemSite_Code', max_length=10, null=True)),
                ('dt_itemno', models.CharField(blank=True, max_length=20, null=True)),
                ('dt_lineno', models.IntegerField(blank=True, db_column='dt_LineNo', null=True)),
                ('lineno', models.IntegerField(blank=True, db_column='LineNo', null=True)),
                ('price', models.FloatField(blank=True, db_column='price', null=True)),
                ('discAmt', models.FloatField(blank=True, db_column='discAmt', null=True)),
                ('discPrice', models.FloatField(blank=True, db_column='discPrice', null=True)),
                ('transacAmount', models.FloatField(blank=True, db_column='transacAmount', null=True)),
                ('depositAmount', models.FloatField(blank=True, db_column='depositAmount', null=True)),
                ('newPrice', models.FloatField(blank=True, db_column='newPrice', null=True)),
                ('newDiscAmt', models.FloatField(blank=True, db_column='newDiscAmt', null=True)),
                ('newDiscPrice', models.FloatField(blank=True, db_column='newDiscPrice', null=True)),
                ('newTransacAmount', models.FloatField(blank=True, db_column='newTransacAmount', null=True)),
                ('newDepositAmount', models.FloatField(blank=True, db_column='newDepositAmount', null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'priceChangeLog',
            },
        ),
    ]
