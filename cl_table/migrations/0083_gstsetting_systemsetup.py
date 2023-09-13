# Generated by Django 3.0.7 on 2023-07-17 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0082_systemlog_systemloginlog'),
    ]

    operations = [
        migrations.CreateModel(
            name='GstSetting',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('item_code', models.CharField(blank=True, db_column='ITEM_CODE', max_length=50, null=True)),
                ('item_desc', models.CharField(blank=True, db_column='ITEM_DESC', max_length=50, null=True)),
                ('item_value', models.FloatField(blank=True, db_column='ITEM_VALUE', null=True)),
                ('isactive', models.BooleanField(blank=True, db_column='ISACTIVE', default=True, null=True)),
                ('item_seq', models.FloatField(blank=True, db_column='ITEM_SEQ', null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_exclusive', models.BooleanField(null=True)),
                ('activefromdate', models.DateTimeField(blank=True, db_column='activefromdate', null=True)),
                ('activetodate', models.DateTimeField(blank=True, db_column='activetodate', null=True)),
            ],
            options={
                'db_table': 'GST_Setting',
            },
        ),
        migrations.CreateModel(
            name='Systemsetup',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, db_column='Title', max_length=100, null=True)),
                ('value_name', models.CharField(blank=True, db_column='Value_name', max_length=200, null=True)),
                ('value_data', models.CharField(blank=True, db_column='Value_data', max_length=300, null=True)),
                ('limit_choice', models.CharField(blank=True, db_column='Limit_choice', max_length=100, null=True)),
                ('long_remarks', models.CharField(blank=True, db_column='Long_Remarks', max_length=1000, null=True)),
                ('short_remarks', models.CharField(blank=True, db_column='Short_Remarks', max_length=300, null=True)),
                ('use_function', models.CharField(blank=True, db_column='Use_Function', max_length=100, null=True)),
                ('create_datetime', models.DateTimeField(auto_now_add=True, db_column='Create_DateTime', null=True)),
                ('edit_datetime', models.DateTimeField(auto_now_add=True, db_column='Edit_DateTime', null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('isactive', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'SystemSetup',
            },
        ),
    ]
