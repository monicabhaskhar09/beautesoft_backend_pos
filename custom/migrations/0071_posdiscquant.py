# Generated by Django 3.0.7 on 2023-07-17 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0070_equipmentdropdownmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='PosDiscQuant',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('invoice_no', models.CharField(max_length=500, null=True)),
                ('dt_itemno', models.CharField(db_column='dt_ItemNo', max_length=50, null=True)),
                ('disc_amt', models.FloatField(blank=True, db_column='Disc_Amt', null=True)),
                ('disc_percent', models.FloatField(blank=True, db_column='Disc_Percent', null=True)),
                ('dt_lineno', models.IntegerField(db_column='dt_LineNo', null=True)),
                ('remark', models.CharField(blank=True, db_column='Remark', max_length=200, null=True)),
                ('site_code', models.CharField(db_column='Site_Code', max_length=50, null=True)),
                ('dt_date', models.DateTimeField(auto_now_add=True, db_column='dt_Date', null=True)),
                ('dt_status', models.CharField(max_length=50, null=True)),
                ('dt_auto', models.BooleanField(db_column='dt_Auto', null=True)),
                ('line_no', models.IntegerField(db_column='Line_no', null=True)),
                ('disc_user', models.CharField(blank=True, db_column='Disc_User', max_length=250, null=True)),
                ('lnow', models.BooleanField(db_column='lNow', null=True)),
                ('dt_price', models.FloatField(blank=True, db_column='dt_Price', null=True)),
                ('istransdisc', models.BooleanField(db_column='IsTransDisc', null=True)),
            ],
            options={
                'db_table': 'Pos_DiscQuant',
            },
        ),
    ]
