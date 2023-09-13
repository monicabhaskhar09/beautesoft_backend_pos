# Generated by Django 3.0.7 on 2023-07-17 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0097_dailysalesdatasummary'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailysalestdSummary',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('sitecode', models.CharField(db_column='SiteCode', max_length=20)),
                ('business_date', models.DateTimeField(db_column='Business_Date')),
                ('helper_code', models.CharField(blank=True, db_column='Helper_Code', max_length=20, null=True)),
                ('daily_share_count', models.FloatField(blank=True, db_column='Daily_Share_Count', null=True)),
                ('daily_share_amount', models.FloatField(blank=True, db_column='Daily_Share_Amount', null=True)),
                ('lastupdate', models.DateTimeField(db_column='LastUpDate')),
            ],
            options={
                'db_table': 'DailySalesTD_Summary',
            },
        ),
    ]
