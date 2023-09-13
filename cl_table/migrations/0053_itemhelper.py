# Generated by Django 3.0.7 on 2023-07-17 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0052_tmpmultistaff'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemHelper',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('item_code', models.CharField(db_column='Item_Code', max_length=20, null=True)),
                ('item_name', models.CharField(blank=True, db_column='Item_Name', max_length=100, null=True)),
                ('line_no', models.IntegerField(db_column='Line_No', null=True)),
                ('sa_transacno', models.CharField(max_length=20, null=True)),
                ('amount', models.FloatField(blank=True, db_column='Amount', null=True)),
                ('helper_name', models.CharField(blank=True, db_column='Helper_Name', max_length=600, null=True)),
                ('helper_code', models.CharField(db_column='Helper_Code', max_length=200, null=True)),
                ('sa_date', models.DateTimeField(null=True)),
                ('site_code', models.CharField(db_column='Site_code', max_length=10, null=True)),
                ('share_amt', models.FloatField(blank=True, db_column='Share_Amt', null=True)),
                ('helper_transacno', models.CharField(db_column='Helper_transacno', max_length=20, null=True)),
                ('wp1', models.FloatField(blank=True, db_column='WP1', null=True)),
                ('wp2', models.FloatField(blank=True, db_column='WP2', null=True)),
                ('wp3', models.FloatField(blank=True, db_column='WP3', null=True)),
                ('percent', models.FloatField(blank=True, db_column='Percent', null=True)),
                ('work_amt', models.FloatField(blank=True, db_column='Work_Amount', null=True)),
                ('session', models.FloatField(blank=True, db_column='Session', null=True)),
                ('times', models.CharField(blank=True, db_column='Times', max_length=10, null=True)),
                ('treatment_no', models.CharField(blank=True, db_column='Treatment_No', max_length=10, null=True)),
            ],
            options={
                'db_table': 'Item_helper',
            },
        ),
    ]