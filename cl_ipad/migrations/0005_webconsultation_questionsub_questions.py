# Generated by Django 3.0.7 on 2023-07-17 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cl_ipad', '0004_webconsultation_questionmultichoice'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebConsultation_Questionsub_questions',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('options', models.CharField(blank=True, db_column='options', max_length=100, null=True)),
                ('sub_question_english', models.CharField(blank=True, db_column='sub_question_english', max_length=500, null=True)),
                ('sub_question_chinese', models.CharField(blank=True, db_column='sub_question_chinese', max_length=500, null=True)),
                ('questionid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cl_ipad.WebConsultation_Question')),
            ],
            options={
                'db_table': 'WebConsultation_Questionsub_questions',
            },
        ),
    ]