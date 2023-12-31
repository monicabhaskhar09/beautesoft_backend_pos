# Generated by Django 3.0.7 on 2023-07-17 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_app', '0013_tmpitemhelpersession'),
        ('cl_ipad', '0002_webconsultation_dtl'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebConsultation_Question',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('question_group', models.CharField(blank=True, db_column='QuestionGroup', max_length=200, null=True)),
                ('question_number', models.IntegerField(blank=True, db_column='QuestionNumber', null=True)),
                ('page_number', models.IntegerField(blank=True, db_column='PageNumber', null=True)),
                ('isactive', models.BooleanField(default=True)),
                ('question_type', models.CharField(blank=True, db_column='QuestionType', max_length=500, null=True)),
                ('image', models.ImageField(blank=True, db_column='image', null=True, upload_to='img')),
                ('question_english', models.CharField(blank=True, db_column='QuestionEnglish', max_length=500, null=True)),
                ('question_chinese', models.CharField(blank=True, db_column='QuestionChinese', max_length=500, null=True)),
                ('question_others', models.CharField(blank=True, db_column='QuestionOthers', max_length=500, null=True)),
                ('question_text', models.CharField(blank=True, db_column='QuestionText', max_length=500, null=True)),
                ('option_type', models.IntegerField(blank=True, db_column='option_type', null=True)),
                ('mandatory', models.BooleanField(db_column='Mandatory', default=False)),
                ('declaration_text', models.TextField(blank=True, db_column='Declaration_Text', null=True)),
                ('site_ids', models.ManyToManyField(blank=True, to='cl_app.ItemSitelist')),
            ],
            options={
                'db_table': 'WebConsultation_Question',
            },
        ),
    ]
