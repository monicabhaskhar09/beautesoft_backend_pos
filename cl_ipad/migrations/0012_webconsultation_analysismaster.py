# Generated by Django 3.0.7 on 2023-09-04 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_ipad', '0011_tnc_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebConsultation_AnalysisMaster',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('field_name', models.CharField(blank=True, db_column='fieldName', max_length=100, null=True)),
                ('display_field_name', models.CharField(blank=True, db_column='displayFieldName', max_length=100, null=True)),
                ('choice_name', models.CharField(blank=True, db_column='choiceName', max_length=100, null=True)),
                ('isactive', models.BooleanField(db_column='IsActive', default=True)),
                ('header', models.BooleanField(db_column='header', default=False)),
                ('body', models.BooleanField(db_column='body', default=False)),
                ('footer', models.BooleanField(db_column='footer', default=False)),
                ('mandatory', models.BooleanField(db_column='Mandatory', default=False)),
                ('image', models.ImageField(blank=True, db_column='image', null=True, upload_to='img')),
                ('is_image', models.BooleanField(db_column='is_image', default=False)),
                ('seq', models.IntegerField(blank=True, db_column='Seq', null=True)),
            ],
            options={
                'db_table': 'WebConsultation_AnalysisMaster',
            },
        ),
    ]