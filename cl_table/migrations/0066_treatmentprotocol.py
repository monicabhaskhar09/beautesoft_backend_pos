# Generated by Django 3.0.7 on 2023-07-17 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_table', '0065_stktrn'),
    ]

    operations = [
        migrations.CreateModel(
            name='TreatmentProtocol',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('item_code', models.CharField(blank=True, db_column='ITEM_CODE', max_length=20, null=True)),
                ('protocol_detail', models.TextField(blank=True, db_column='Protocol_Detail', null=True)),
                ('protocol_duration', models.TextField(blank=True, db_column='Protocol_Duration', null=True)),
                ('line_no', models.IntegerField(blank=True, db_column='Line_No', null=True)),
                ('isactive', models.BooleanField(db_column='ISACTIVE', default=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'Treatment_Protocol',
            },
        ),
    ]
