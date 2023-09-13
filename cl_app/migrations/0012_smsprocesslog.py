# Generated by Django 3.0.7 on 2023-07-17 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_app', '0011_voucherpromo'),
    ]

    operations = [
        migrations.CreateModel(
            name='SmsProcessLog',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('sms_username', models.CharField(blank=True, db_column='SMS_UserName', max_length=100, null=True)),
                ('sms_password', models.CharField(blank=True, db_column='SMS_Password', max_length=100, null=True)),
                ('sms_phone', models.CharField(blank=True, db_column='SMS_Phone', max_length=300, null=True)),
                ('sms_msg', models.CharField(blank=True, db_column='SMS_Msg', max_length=1000, null=True)),
                ('sms_datetime', models.DateTimeField(blank=True, db_column='SMS_DateTime', null=True)),
                ('send_status', models.CharField(blank=True, db_column='Send_Status', max_length=100, null=True)),
                ('send_datetime', models.DateTimeField(blank=True, db_column='Send_DateTime', null=True)),
                ('site_code', models.CharField(blank=True, db_column='Site_Code', max_length=20, null=True)),
                ('vendor_type', models.CharField(blank=True, db_column='Vendor_Type', max_length=20, null=True)),
                ('smsapireply', models.CharField(blank=True, db_column='SMSApiReply', max_length=800, null=True)),
                ('isactive', models.BooleanField(blank=True, db_column='IsActive', null=True)),
                ('sms_task_number', models.CharField(blank=True, db_column='SMS_Task_Number', max_length=10, null=True)),
                ('sms_portno', models.CharField(blank=True, db_column='SMS_PortNo', max_length=10, null=True)),
                ('sms_sendername', models.CharField(blank=True, db_column='SMS_SenderName', max_length=100, null=True)),
                ('sms_campaignname', models.CharField(blank=True, db_column='SMS_CampaignName', max_length=100, null=True)),
                ('sms_scheduleid', models.IntegerField(blank=True, db_column='SMS_ScheduleID', null=True)),
                ('sms_type', models.CharField(blank=True, db_column='SMS_Type', max_length=100, null=True)),
            ],
            options={
                'db_table': 'SMS_Process_Log',
            },
        ),
    ]